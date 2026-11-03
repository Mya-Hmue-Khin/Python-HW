pet_one = {"mainecoon cat": "john"}
pet_two = {"chihuahua": "karen"}
pet_three = {"poodle": "aisha"}

pets = [pet_one, pet_two, pet_three]
for pet in pets:
    for k, v in pet.items():
        print(f"{k.title()}'s owner is {v.title()}.")
