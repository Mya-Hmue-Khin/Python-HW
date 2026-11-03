pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 'size': 'large',
 'price': '15$'
 }
print(f"You ordered the {pizza['size']} size, {pizza['crust']}-crusted pizza with the followinf toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
print(f"That will be {pizza['price']}. Thank you!")