fav_places = {"bryan": ["Hôtel des Invalides", "Fuji"], 
              "amara": ["Bagan", "Taunggyi"], 
              "melia": ["Mauritius", "Grand Canyon", "Giza"]}
for k, v in fav_places.items():
    for places in v:
        print(f"{k.title()}'s favourite place is {v}.")
