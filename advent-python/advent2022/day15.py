from typing import NamedTuple
from sys import exit

#Represent a range of integers, endpoint-inclusive
class IntRange(NamedTuple):
    min: int
    max: int

    def intersects(self: IntRange, other: IntRange) -> bool:
        return self.min <= other.min <= self.max or other.min <= self.min <= other.max
    
    def union(self: IntRange, other: IntRange) -> IntRange:
        if not self.intersects(other):
            raise ValueError("ranges do not intersect")
        return IntRange(min(self.min, other.min), max(self.max, other.max))
    
    def remove_point(self: IntRange, num: int) -> list[IntRange]:
        if num not in self:
            return [self]
        elif num == self.min and num == self.max:
            return []
        elif num == self.min:
            return [IntRange(self.min+1, self.max)]
        elif num == self.max:
            return [IntRange(self.min, self.max-1)]
        else:
            return [IntRange(self.min, num-1), IntRange(num+1, self.max)]
    
    def __len__(self: IntRange) -> int:
        return self.max - self.min + 1
    
    def __contains__(self: IntRange, other: object) -> bool:
        if isinstance(other, int):
            return self.min <= other <= self.max
        else:
            return False
    
def merge_intervals(intervals: list[IntRange]) -> list[IntRange]:
    prev_intervals: list[IntRange] = []
    while prev_intervals != intervals:
        prev_intervals = intervals
        intervals = []
        for interval in prev_intervals:
            for i, interval_2 in enumerate(intervals):
                if interval.intersects(interval_2):
                    intervals[i] = interval_2.union(interval)
                    break
            else:
                intervals.append(interval)
    return intervals

def delete_points(intervals: list[IntRange], points: list[int]) -> list[IntRange]:
    prev_intervals: list[IntRange] = []
    for point in points:
        prev_intervals = intervals
        intervals = []
        for interval in prev_intervals:
            for new_interval in interval.remove_point(point):
                intervals.append(new_interval)
    return intervals

def impossible_xs(y: int, sensors: dict[tuple[int, int], tuple[int, int]]) -> int:
    beacons_in_row: list[int] = []
    intervals: list[IntRange] = []
    for (s_x, s_y), (b_x, b_y) in sensors.items():
        distance: int = abs(s_x-b_x) + abs(s_y-b_y)
        if b_y == y:
            beacons_in_row.append(b_x)
        if abs(s_y - y) > distance:
            continue
        intervals.append(IntRange(s_x-(distance - abs(s_y-y)), s_x + (distance-abs(s_y-y))))
    
    intervals = delete_points(intervals, beacons_in_row)
    return sum(len(interval) for interval in merge_intervals(intervals))

#generates points that are one square too far away from (x,y) to be detected
def one_too_far(x: int, y: int, radius: int):
    yield (x+radius+1, y)
    yield (x-(radius+1), y)
    yield (x, y+radius+1)
    yield (x, y-radius-1)
    for i in range(1, radius+1):
        yield (x+i, y+(radius+1-i))
        yield (x-i, y+(radius+1-i))
        yield (x+i, y-(radius+1-i))
        yield (x-i, y-(radius+1-i))

def in_range(x1: int, y1: int, x2: int, y2: int, radius: int) -> bool:
    return abs(x1-x2) + abs(y1-y2) <= radius

with open("input-15.txt") as f:
    data: list[str] = [line.strip() for line in f]

beacons_in_row: list[int] = []
sensors: dict[tuple[int, int], tuple[int, int]] = {}
for line in data:
    split: list[str] = line.split()
    sensor_x: int = int(split[2][2:-1])
    sensor_y: int = int(split[3][2:-1])
    beacon_x: int = int(split[8][2:-1])
    beacon_y: int = int(split[9][2:])
    sensors[(sensor_x, sensor_y)] = (beacon_x, beacon_y)

#Part 1
print(impossible_xs(2000000, sensors))

#Part 2
#If only one point in the region is viable, it must be exactly one square out of range of at least one sensor
#We check all such points until we find one that isn't in range of any sensor
max_coord: int = 4000000
sensor_set: set[tuple[int, int]] = set(sensors.keys())
beacon_set: set[tuple[int, int]] = set(sensors.values())
for (sensor_x, sensor_y), (beacon_x, beacon_y) in sensors.items():
    print(f"Testing points on edge of {sensor_x}, {sensor_y}")
    radius: int = abs(sensor_x-beacon_x) + abs(sensor_y-beacon_y)
    for i, (x,y) in enumerate(one_too_far(sensor_x, sensor_y, radius)):
        if i%1000 == 0:
            print(f"Testing {i+1} of {4*radius}")
        if 0 <= x <= max_coord and 0 <= y <= max_coord and (x,y) not in sensors and (x,y) not in sensors.values():
            found: bool = True
            for (s_x, s_y), (b_x, b_y) in sensors.items():
                radius_2: int = abs(s_x-b_x)+abs(s_y-b_y)
                if in_range(x, y, s_x, s_y, radius_2):
                    found = False
            if found:
                print(4000000*x+y)
                exit(0)