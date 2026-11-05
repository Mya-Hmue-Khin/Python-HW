sandwich_orders = ["grilled cheese", "egg salad sandwich", "tuna salad sandwich"]
finished_sandwiches = []
while sandwich_orders:
    popped_sandwiches = sandwich_orders.pop()
    print(f"I made you {popped_sandwiches.title()}")
    finished_sandwiches.append(popped_sandwiches)