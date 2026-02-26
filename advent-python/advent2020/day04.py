with open("input-04.txt") as f:
    data: list[str] = [line.strip() for line in f]

REQUIRED_FIELDS: list[str] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
def required_fields_present(passport: dict[str, str]) -> bool:
    for field in REQUIRED_FIELDS:
        if field not in passport:
            return False
    return True

def valid_passport(passport: dict[str, str]) -> bool:
    if not required_fields_present(passport):
        return False
    if not valid_birth_year(passport["byr"]):
        return False
    if not valid_issue_year(passport["iyr"]):
        return False
    if not valid_expiration_year(passport["eyr"]):
        return False
    if not valid_height(passport["hgt"]):
        return False
    if not valid_hair_color(passport["hcl"]):
        return False
    if not valid_eye_color(passport["ecl"]):
        return False
    if not valid_passport_id(passport["pid"]):
        return False
    return True

def valid_birth_year(byr: str) -> bool:
    return len(byr) == 4 and byr.isnumeric() and 1920 <= int(byr) <= 2002

def valid_issue_year(iyr: str) -> bool:
    return len(iyr) == 4 and iyr.isnumeric() and 2010 <= int(iyr) <= 2020

def valid_expiration_year(eyr: str) -> bool:
    return len(eyr) == 4 and eyr.isnumeric() and 2020 <= int(eyr) <= 2030

def valid_height(hgt: str) -> bool:
    if len(hgt) < 2:
        return False
    elif hgt[-2:] == "in":
        return hgt[:-2].isnumeric() and 59 <= int(hgt[:-2]) <= 76
    elif hgt[-2:] == "cm":
        return hgt[:-2].isnumeric() and 150 <= int(hgt[:-2]) <= 193
    else:
        return False

def valid_hair_color(hcl: str) -> bool:
    if len(hcl) != 7:
        return False
    elif hcl[0] != "#":
        return False
    else:
        for char in hcl[1:]:
            if char not in "0123456789abcdef":
                return False
        return True
    
def valid_eye_color(ecl: str):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid_passport_id(pid: str):
    return len(pid) == 9 and pid.isnumeric()



#Part 1
valid_count: int = 0

working_data: list[str] = list(data)
current_passport: dict[str, str] = {}
while len(working_data) > 0:
    line: str = working_data.pop(0)
    if line == "":
        if required_fields_present(current_passport):
            valid_count += 1
        current_passport = {}
    else:
        line_split: list[str] = line.split()
        for entry in line_split:
            current_passport[entry[:entry.index(":")]] = entry[entry.index(":")+1:]

if required_fields_present(current_passport):
    valid_count += 1

print(valid_count)

#Part 2
valid_count = 0

working_data = list(data)
current_passport = {}
while len(working_data) > 0:
    line: str = working_data.pop(0)
    if line == "":
        if valid_passport(current_passport):
            valid_count += 1
        current_passport = {}
    else:
        line_split: list[str] = line.split()
        for entry in line_split:
            current_passport[entry[:entry.index(":")]] = entry[entry.index(":")+1:]

if valid_passport(current_passport):
    valid_count += 1

print(valid_count)