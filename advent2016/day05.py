from hashlib import md5
from random import choice
from typing import List


PW_BASE: str = "uqwqemis"
HEX_DIGITS: str = "01234567abcdef"

def cinematic_password(password: List[str]) -> str:
    return "".join([choice(HEX_DIGITS) if char == '?' else char for char in password])

password: str = ""
i: int = 0
while len(password) < 8:
    next_id: bytes = bytes(PW_BASE + str(i), encoding='ascii')
    hash: str = md5(next_id).hexdigest()
    if hash.startswith("00000"):
        password += hash[5]
        print(f"Next character found at i={i}, current password {password}")
    i+=1

print(password)

#Part 2
password_p2 = ["?"]*8
POS_DIGITS: str = "01234567"
i = 0
digits_found: int = 0
while digits_found < 8:
    next_id = bytes(PW_BASE + str(i), encoding='ascii')
    hash = md5(next_id).hexdigest()
    if hash.startswith("00000"):
        #print(f"Possible match found at i={i}: Hash={hash}")
        if hash[5] in POS_DIGITS and password_p2[int(hash[5])] == "?":
            password_p2[int(hash[5])] = hash[6]
            digits_found += 1
            print(cinematic_password(password_p2))
    i += 1
    if i%50000 == 0:
        print(cinematic_password(password_p2))

