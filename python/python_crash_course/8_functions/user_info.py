#Testing something about mixing arguments.

def build_profile(**user_info):
    return user_info

user_profile = build_profile(first='Lionel', last='Messi', age=39, occupation='footballer')
for key, value in user_profile.items():
    print(f"{key}: {value}")
