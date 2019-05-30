#! /usr/bin/env python

with open('14-input.txt', 'r') as f:
    recipe_count = f.read()

recipe_count = int(recipe_count)

original_recipes = [3, 7]
first_elf_at = 0
second_elf_at = 1

recipes = original_recipes

while len(recipes) < recipe_count + 10:
    new_recipes = recipes[first_elf_at] + recipes[second_elf_at]

    if new_recipes > 9:
        recipes.append(new_recipes // 10)
    recipes.append(new_recipes % 10)

    first_elf_at = ((1
                     + first_elf_at
                     + recipes[first_elf_at])
                    % len(recipes))
    second_elf_at = ((1
                      + second_elf_at
                      + recipes[second_elf_at])
                     % len(recipes))

print(recipes[recipe_count:recipe_count + 10])
