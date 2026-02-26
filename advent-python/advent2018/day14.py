PUZZLE_INPUT: str = "110201"
puzzle_input_int: int = int(PUZZLE_INPUT)

#Part 1
recipes: list[int] = [3, 7]
elf_1_pos: int = 0
elf_2_pos: int = 1

while len(recipes) < puzzle_input_int + 10:
    next_recipes: int = recipes[elf_1_pos] + recipes[elf_2_pos]
    if next_recipes >= 10:
        recipes.append(next_recipes // 10)
    recipes.append(next_recipes % 10)
    elf_1_pos = (elf_1_pos + 1+recipes[elf_1_pos]) % len(recipes)
    elf_2_pos = (elf_2_pos + 1+recipes[elf_2_pos]) % len(recipes)

print("".join([str(x) for x in recipes[-10:]]))

#Part 2
puzzle_input_list = [int(x) for x in PUZZLE_INPUT]
recipes = [3,7]
elf_1_pos = 0
elf_2_pos = 1

iterations = 0
while recipes[-len(puzzle_input_list):] != puzzle_input_list:
    next_recipes = recipes[elf_1_pos] + recipes[elf_2_pos]
    if next_recipes >= 10:
        recipes.append(next_recipes // 10)
        if recipes[-len(puzzle_input_list):] == puzzle_input_list:
            break
    recipes.append(next_recipes % 10)
    elf_1_pos = (elf_1_pos + 1+recipes[elf_1_pos]) % len(recipes)
    elf_2_pos = (elf_2_pos + 1+recipes[elf_2_pos]) % len(recipes)

print(len(recipes) - len(puzzle_input_list))