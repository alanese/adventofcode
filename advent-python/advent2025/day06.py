def product(nums):
    if len(nums) == 0:
        return 1
    else:
        prod = nums[0]
        for num in nums[1:]:
            prod *= num
        return prod

with open("input-06.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]

operators = lines[-1]
columns = [ [int(line[i]) for line in lines[:-1]] for i in range(len(lines[0]))]

total = 0
for op, col in zip(operators, columns):
    if op == "+":
        total += sum(col)
    elif op == "*":
        total += product(col)
    else:
        print("Error:", op)
print(total)

#---------
with open("input-06.txt") as f:
    lines = [line for line in f.readlines()]

operators = lines[-1].split()

rows = lines[:-1]
max_length = max([len(row) for row in rows])
for i in range(len(rows)):
    rows[i] = rows[i] + " "*(max_length - len(rows[i]))

columns = [ [row[i] for row in rows] for i in range(max_length) ]
columns = [ "".join(digits).strip() for digits in columns]

problems = []
next_problem = []
for number in columns:
    if number == "":
        problems.append(next_problem)
        next_problem = []
    else:
        next_problem.append(int(number))
if len(next_problem) != 0:
    problems.append(next_problem)

total = 0
for op, numbers in zip(operators, problems):
    if op == "+":
        total += sum(numbers)
    elif op == "*":
        total += product(numbers)
    else:
        print(f"Error - {op} not a recognized operator")
print(total)