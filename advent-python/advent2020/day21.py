from typing import NamedTuple
from collections import defaultdict

class Recipe(NamedTuple):
    ingredients: set[str]
    allergens: set[str]

def parse_recipe(line: str) -> Recipe:
    ingredients, _, allergens = line[:-1].partition(" (contains ")
    return Recipe(set(ingredients.split()), set(allergens.split(", ")))

with open("input-21.txt") as f:
    data: list[str] = [line.strip() for line in f]

recipes: list[Recipe] = []

ingredients: set[str] = set()
allergens: set[str] = set()

#Key is allergen, value is set of ingredients that could contain it
possible_allergens: dict[str, set[str]] = defaultdict(set)
for line in data:
    recipe: Recipe = parse_recipe(line)
    ingredients |= recipe.ingredients
    allergens |= recipe.allergens
    for allergen in recipe.allergens:
        for ingredient in recipe.ingredients:
            possible_allergens[allergen].add(ingredient)
    recipes.append(recipe)

for recipe in recipes:
    for allergen in recipe.allergens:
        possible_allergens[allergen] &= recipe.ingredients

allergen_free: set[str] = ingredients.copy()
for ings in possible_allergens.values():
    allergen_free -= ings

count: int = 0
for recipe in recipes:
    count += len(allergen_free & recipe.ingredients)
print(count)

#Part 2

#Key is allergen, value is ingredient
fixed_allergens: dict[str, str] = {}

while len(possible_allergens) > 0:
    for allergen, ing_set in possible_allergens.items():
        if len(ing_set) == 1:
            ing: str = ing_set.pop()
            fixed_allergens[allergen] = ing
            del possible_allergens[allergen]
            for ings in possible_allergens.values():
                ings.discard(ing)
            break

print (",".join(v for (k,v) in sorted(fixed_allergens.items())))
