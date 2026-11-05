prompt = "Enter the toppings"
prompt += "\nEnter quit when you're finished."

active = True
while active:
    toppings = input(prompt)
    if toppings == "quit":
        active = False
    else:
        print(toppings)