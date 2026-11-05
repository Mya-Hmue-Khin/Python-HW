sandwich_orders = ["grilled cheese", "pastrami",
                   "egg salad sandwich", "pastrami", "tuna salad sandwich", "pastrami"]
finished_sandwiches = []
print("The deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    popped_sandwiches = sandwich_orders.pop()
    print(f"I made you {popped_sandwiches.title()}")
    finished_sandwiches.append(popped_sandwiches)
print(finished_sandwiches)