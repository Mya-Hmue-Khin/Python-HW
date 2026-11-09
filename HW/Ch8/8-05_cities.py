def describe_city(name_of_the_city, country_of_the_city='Japan'):
    print(f"{name_of_the_city.title()} is the city of {country_of_the_city}.")

describe_city('tokyo')
describe_city('osaka')
describe_city('Seoul', country_of_the_city='Korea')