rivers = {"nile": "egypt", "amazon": "brazil", "yangtze": "china"}
for k, v in rivers.items():
    print(f"The {k.title()} River flows across {v.title()} shaping the surrounding natural environment and ecosystems.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
