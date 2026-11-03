cities = {"tokyo": {"country": "japan", "population": "37.4 million",
                     "fact": "home to Shibuya Crossing, the busiest pedestrian intersection in the world, handling up to 3,000 people per green light."},
          "são paulo": {"country": "brazil", "population": "22.5 million",
                                    "fact": "home to the largest helicopter fleet in the world, using over 200 helipads to bypass severe traffic congestion."}, 
            "cairo": {"country": "egypt", "population": "22.1 million", 
                    "fact": "home to Al-Azhar University, one of the oldest operating universities in the world, founded in 970 CE."}}
for city_name, city_info in cities.items():
    print(f"{city_name.title()}:")
    print(f"City of {city_info['country'].title()}, has {city_info['population'].title()}, and {city_info['fact'].title()}")