first_info = {"first_name": "Nge",
              "last_name": "Nge", "age": 19, "city": "Yangon"}
second_info = {"first_name": "Kue",
               "last_name": "Kue", "age": 23, "city": "Mandalay"}
third_info = {"first_name": "Lila",
              "last_name": "Van", "age": 16, "city": "Bago"}


people = [first_info, second_info, third_info]
for i in people:
    for k, v in i.items():
        print(f"{k}: {v}")
