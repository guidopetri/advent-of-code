#! /usr/bin/env python

with open('14-input.txt', 'r') as f:
    recipe_sequence = f.read()

recipe_sequence = list(recipe_sequence)
recipe_sequence = [int(x) for x in recipe_sequence]

original_recipes = [3, 7]
first_elf_at = 0
second_elf_at = 1

recipes = original_recipes

minus_one = False

while True:
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

    if recipes[-len(recipe_sequence):] == recipe_sequence:
        break
    elif recipes[-len(recipe_sequence) - 1:-1] == recipe_sequence:
        minus_one = True
        break

if minus_one:
    print(len(recipes) - len(recipe_sequence) - 1)
else:
    print(len(recipes) - len(recipe_sequence))
