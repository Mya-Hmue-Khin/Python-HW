current_users = ["zen_flow44", "nova_spark11",
                 "shadow_leaf03", "urban_wave77", "solar_pulse50"]
current_users_lower = [user.lower() for user in current_users]
new_users = ["nova_spark11", "velvet_glow18",
             "mellow_breeze09", "solar_pulse50", "Shadow_Leaf03"]
for user in new_users:
    if user.lower() in current_users_lower:
        print("the username already existed!")
    else:
        print("the username is available!")
