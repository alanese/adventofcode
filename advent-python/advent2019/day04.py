INPUT_DATA = "271973-785961"

def valid_password(password: str) -> bool:
    doubles: bool = False
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            return False
        if password[i] == password[i+1]:
            doubles = True
    return doubles

def valid_password_p2(password: str) -> bool:
    doubles: bool = False
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            return False
        if password[i] == password[i+1] and (i+2 >= len(password) or password[i+1] != password[i+2]) and (i <= 0 or password[i] != password[i-1]):
            doubles = True
    return doubles

#Part 1
bounds: list[int] = [int(x) for x in INPUT_DATA.split("-")]
valid_count: int = 0
for i in range(bounds[0], bounds[1]+1):
    if valid_password(str(i)):
        valid_count += 1
print(valid_count)

#Part 2
bounds = [int(x) for x in INPUT_DATA.split("-")]
valid_count = 0
for i in range(bounds[0], bounds[1]+1):
    if valid_password_p2(str(i)):
        valid_count += 1
print(valid_count)

