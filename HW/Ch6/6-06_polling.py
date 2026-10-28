favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

voting_list = ["jen", "sofia", "sarah", "edward", "catalina", "phil"]
for names in voting_list:
    if names in favorite_languages:
        print(f"Thank you, {names.title()}!")
    else:
        print("you are invited to vote!")
