from collections import defaultdict

def parse_guard_schedules(data: list[str]) -> dict[int, list[int]]:
    sorted_data: list[str] = sorted(data)
    guards: dict[int, list[int]] = defaultdict(lambda: [0]*60)

    split_line: list[str] = sorted_data[0].split()
    guard_id: int = int(split_line[3][1:])
    sleep_start_time = 0
    currently_asleep: bool = False
    for line in sorted_data[1:]:
        split_line = line.split()
        match split_line[2]:
            case "Guard":
                if currently_asleep:
                    for minute in range(sleep_start_time, 60):
                        guards[guard_id][minute] += 1
                guard_id = int(split_line[3][1:])
                currently_asleep = False
                sleep_start_time = 0
            case "falls":
                sleep_start_time = int(split_line[1][3:5])
                currently_asleep = True
            case "wakes":
                for minute in range(sleep_start_time, int(split_line[1][3:5])):
                    guards[guard_id][minute] += 1
                currently_asleep = False
    return guards

with open("input-04.txt") as f:
    data: list[str] = [line.strip() for line in f]


#Part 1
guards: dict[int, list[int]] = parse_guard_schedules(data)
max_sleep_pattern: list[int] = []
sleepiest_guard: int = 0
for guard, minutes in guards.items():
    if sum(minutes) > sum(max_sleep_pattern):
        max_sleep_pattern = minutes
        sleepiest_guard = guard

common_minute: int = 0
common_minute_count: int = 0
for i, count in enumerate(max_sleep_pattern):
    if count > common_minute_count:
        common_minute = i
        common_minute_count = count

print(sleepiest_guard * common_minute)

#Part 2
guards = parse_guard_schedules(data)
sleepiest_minute: int = 0
sleepiest_minute_count: int = 0
sleepiest_guard = 0
for guard, minutes in guards.items():
    for minute, count in enumerate(minutes):
        if count > sleepiest_minute_count:
            sleepiest_minute_count = count
            sleepiest_minute = minute
            sleepiest_guard = guard

print(sleepiest_guard * sleepiest_minute)