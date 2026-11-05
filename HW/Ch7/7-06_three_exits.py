# using conditional test
prompt = "Enter the toppings"
prompt += "\nEnter quit when you're finished."

message = ""
while message != "quit":
    message = input(prompt)
    print(message)

# using active variable
prompt = "Enter the toppings"
prompt += "\nEnter quit when you're finished."

active = True
while active:
    toppings = input(prompt)
    if toppings == "quit":
        active = False
    else:
        print(toppings)

# using break
prompt = "Enter the toppings"
prompt += "\nEnter quit when you're finished."

active = True
while active:
    toppings = input(prompt)
    if toppings == "quit":
        break
    else:
        print(f"Got it! Adding {toppings} right away.")
