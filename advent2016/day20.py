from typing import NamedTuple

class Interval(NamedTuple):
    low: int
    high: int

def check_intersect(interval1: Interval, interval2: Interval) -> bool:
    return interval1.low <= interval2.low <= interval1.high or interval2.low <= interval1.low <= interval2.high

def intersection(interval1: Interval, interval2: Interval) -> Interval:
    return Interval(max(interval1.low, interval2.low), min(interval1.high, interval2.high))

IP_MIN = 0
IP_MAX = 2**32 - 1
def invert_interval(interval: Interval) -> list[Interval]:
    if interval.low == IP_MIN and interval.high == IP_MAX:
        return []
    elif interval.low == IP_MIN:
        return [Interval(interval.high+1, IP_MAX)]
    elif interval.high == IP_MAX:
        return [Interval(IP_MIN, interval.low-1)]
    else:
        return [Interval(IP_MIN, interval.low-1), Interval(interval.high+1, IP_MAX)]
    
def parse_interval(interval: str) -> Interval:
    split = interval.split("-")
    return Interval(int(split[0]), int(split[1]))

def interval_length(interval: Interval) -> int:
    return interval.high - interval.low + 1

valid_ranges: list[Interval] = [Interval(IP_MIN, IP_MAX)]
with open("input-20.txt") as f:
    for line in f:
        new_valid_ranges: list[Interval] = []
        blacklist_range: Interval = parse_interval(line.strip())
        ok_ranges: list[Interval] = invert_interval(blacklist_range)
        for valid in valid_ranges:
            for ok in ok_ranges:
                if check_intersect(valid, ok):
                    new_valid_ranges.append(intersection(valid, ok))
        valid_ranges = new_valid_ranges

print(min([interval.low for interval in valid_ranges]))
print(sum([interval_length(interval) for interval in valid_ranges]))