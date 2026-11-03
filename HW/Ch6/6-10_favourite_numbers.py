fav_nums = {"mya": [1, 8], "cristine": [2, 7, 9], "tom": [3, 9], "luna": [5, 23], "catalina": [7, 8]}
for names, numbers in fav_nums.items():
    print(f"{names.title()}'s favourite numbers:")
    for number in numbers:
        print(f"\t{number}")