def safe_report_v1(report: list[int]) -> bool:
    diffs: list[int] = [report[x] - report[x+1] for x in range(len(report)-1)]
    return all(1<=x<=3 for x in diffs) or all(-3<=x<=-1 for x in diffs)

def safe_report_v2(report: list[int]) -> bool:
    for i in range(len(report)):
        if safe_report_v1(report[:i] + report[i+1:]):
            return True
    return False

with open("input-02.txt") as f:
    data: list[list[int]] = [ [int(x) for x in line.strip().split()] for line in f]

print(sum(safe_report_v1(line) for line in data))
print(sum(safe_report_v2(line) for line in data))