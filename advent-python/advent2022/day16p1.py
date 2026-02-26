import heapq
import pickle
from typing import NamedTuple

VALVE_IDS: dict[str, int]
VALVE_FLOWRATES: tuple[int, ...]
PATHS: dict[str, list[str]]
DISTANCE: dict[str, dict[str, int]]
class State(NamedTuple):
    countdown: int
    dest: str
    elephant_countdown: int
    elephant_dest: str
    time: int
    open_valves: int #bitfield

    def total_flow(self: State) -> int:
        return sum(rate for i, rate in enumerate(VALVE_FLOWRATES) if self.open_valves & 1<<i)

def next_dest_countdown(state: State, forbidden_dest: set[str] = set()) -> list[tuple[str, int]]:
    if state.dest == "STOP":
        return [("STOP", 1)]
    elif state.countdown > 0:
        return [(state.dest, state.countdown-1)]
    else:
        r: list[tuple[str, int]] = []
        for valve, id in VALVE_IDS.items():
            if VALVE_FLOWRATES[id] > 0 and not (state.open_valves & 1<<id) and valve not in forbidden_dest:
                r.append((valve, DISTANCE[state.dest][valve]))
        if len(r) > 0:
            return r
        return [("STOP", 1)]

    
def next_elephant_pos_dest(state: State, forbidden_dest: set[str] = set()) -> list[tuple[str, int]]:
    if state.elephant_dest == "E-STOP":
        return [("E-STOP", 1)]
    elif state.elephant_countdown > 0:
        return [(state.elephant_dest, state.elephant_countdown-1)]
    else:
        r: list[tuple[str, int]] = []
        for valve, id in VALVE_IDS.items():
            if VALVE_FLOWRATES[id] > 0 and not (state.open_valves & 1<<id) and valve not in forbidden_dest:
                r.append((valve, DISTANCE[state.elephant_dest][valve]))
        if len(r) > 0:
            return r
        return [("E-STOP", 1)]
    
def get_next_states(state: State) -> list[State]:
    r: list[State] = []
    for next_dest, next_cd in next_dest_countdown(state, {state.elephant_dest}):
        tmp: int = state.open_valves
        if state.countdown == 0:
            tmp |= 1<<VALVE_IDS[state.dest]
        r.append(State(next_cd, next_dest, state.elephant_countdown, state.elephant_dest, state.time+1, tmp))
    return r

def get_next_elephant_states(state: State) -> list[State]:
    r: list[State] = []
    for next_dest, next_cd in next_dest_countdown(state, {state.elephant_dest}):
        for next_e_dest, next_e_cd in next_elephant_pos_dest(state, {state.dest, next_dest}):
            if next_dest != next_e_dest:
                tmp: int = state.open_valves
                if state.countdown == 0:
                    tmp |= 1<<VALVE_IDS[state.dest]
                if state.elephant_countdown == 0:
                    tmp |= 1<<VALVE_IDS[state.elephant_dest]
                r.append(State(next_cd, next_dest, next_e_cd, next_e_dest, state.time+1, tmp))
    return r

def distance_to(from_: str, to: str) -> int:
    if from_ == to:
        return 0
    visited: dict[str, int] = {}
    to_visit: list[tuple[int, str]] = [(0, from_)]
    while to not in visited and len(to_visit) > 0:
        next_dist, next = heapq.heappop(to_visit)
        if next not in visited:
            visited[next] = next_dist
            for neighbor in PATHS[next]:
                if neighbor not in visited:
                    heapq.heappush(to_visit, (next_dist+1, neighbor))
    if to not in visited:
        raise ValueError(f"from_ {from_} and to {to} not connected")
    return visited[to]

def best_flow(start: State, time_after: int, cache: dict[State, int]) -> int:
    if start in cache:
        return cache[start]
    elif start.time > time_after:
        raise ValueError("Time already passed")
    elif start.time == time_after:
        return start.total_flow()
    else:
        next_states: list[State] = get_next_states(start)
        rv = start.total_flow() + max(best_flow(next_state, time_after, cache) for next_state in next_states)
        if len(next_states) != 1:
            cache[start] = rv
            if len(cache) % 10000 == 0:
                print(f"cache size {len(cache)}")
        return rv

def best_elephant_flow(start: State, time_after: int, cache: dict[State, int]) -> int:
    if start in cache:
        return cache[start]
    elif start.time > time_after:
        raise ValueError("Time already passed")
    elif start.time == time_after:
        return start.total_flow()
    else:
        next_states: list[State] = get_next_elephant_states(start)
        rv = start.total_flow() + max(best_elephant_flow(next_state, time_after, cache) for next_state in next_states)
        if len(next_states) != 1:
            cache[start] = rv
            if len(cache)%10000 == 0:
                print(f"cache size {len(cache)}")
                if len(cache)%10000000 == 0:
                    print("writing cache . . .")
                    with open("cache.pkl", "wb") as f:
                        pickle.dump(cache, f)
        return rv      

with open("input-16.txt") as f:
    data: list[str] = [line.strip() for line in f]

valve_ids: dict[str, int] = {"AA": 0}
all_valves: set[str] = set()
valve_flowrates: list[int] = [0]
PATHS = {}
valve_count: int = 1
for line in data:
    split = line.split(maxsplit=9)
    all_valves.add(split[1])
    if int(split[4][5:-1]) > 0:
        valve_ids[split[1]] = valve_count
        valve_count += 1
        valve_flowrates.append(int(split[4][5:-1]))
    PATHS[split[1]] = split[-1].split(", ")

VALVE_IDS = valve_ids
VALVE_FLOWRATES = tuple(valve_flowrates)
DISTANCE = {}

#fun fact: this code is terrible and I hate it!
for to in VALVE_IDS:
    for from_ in VALVE_IDS:
        if from_ not in DISTANCE:
            DISTANCE[from_] = {}
        DISTANCE[from_][to] = distance_to(from_, to)

start: State = State(0, "AA", 0, "AA", 0, 0)
print(best_flow(start, 30, {}))

try:
    with open("cache.pkl", "rb") as f:
        cache = pickle.load(f)
except FileNotFoundError:
    cache = {}

print(best_elephant_flow(start, 26, cache))