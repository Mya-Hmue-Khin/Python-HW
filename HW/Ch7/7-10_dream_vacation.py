results_of_polls = {}
polling_active = True
while polling_active:
    name = input("Enter your name: ")
    message = input("If you could visit one place in the world, where would you go?")
    results_of_polls[name] = message
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False
    print (results_of_polls)