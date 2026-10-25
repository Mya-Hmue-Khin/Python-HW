pizzas = ["margherita", "pepperoni", "hawaiian"]
friend_pizzas = ["margherita", "pepperoni", "hawaiian"]
pizzas.append("neapolitan")
friend_pizzas.append("chicago deep dish")
print("my favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n")

print("my friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
