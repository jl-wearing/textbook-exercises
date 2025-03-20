current_users = ['marley', 'zoi', 'zazu', 'shepherd', 'phoenix']
new_users = ['zoi', 'zigzoza', 'pupsy']

for user in new_users:
    if user.lower() in current_users:
        print(f'The username, {user}, is already in use. You will need to change it.')
    else:
        print(f'The username, {user}, is not claimed. Lucky you!')