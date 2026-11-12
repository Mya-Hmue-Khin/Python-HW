def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('Mya', 'Hmue Khin', Weight = '50 kg', Height = '162 cm')
print(my_profile)