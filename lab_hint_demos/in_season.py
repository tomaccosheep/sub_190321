# in_season.py
import random
food_list = ['squash soup', 'bacon-wrapped figs']
ingredient_list = ['squash', 'figs']
chosen_food = input(f"What would you like to make, {food_list[0]} or {food_list[1]}? >")
in_season = random.choice(ingredient_list)
print(f"{in_season} are in season.")
if in_season == ingredient_list[0]:
    if chosen_food == food_list[0]:
        print("You can make squash soup!")
    if chosen_food == food_list[1]:
        print("Too bad sucka")
#if in_season == 'figs':
else:
    if chosen_food == food_list[0]:
        print("Not gonna happen")
    else:
        print("Yay! Have some figs!")
