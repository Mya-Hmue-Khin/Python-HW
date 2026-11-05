prompt = "Enter your age: "
Active = True
while Active:
    ages = input(prompt)
    int_ages = int(ages)
    if int_ages <= 3:
        print("The ticket is free for you!")
        break
    elif int_ages >=3 and int_ages <=12:
        print("Your ticket will cost 10$.")
        break
    else:
        print("Your ticket will cost 15$.")
        break