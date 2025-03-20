usernames = ['admin', 'kiwi', 'nala', 'ziggy', 'aron']

if usernames:
    for name in usernames:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f"Hello {name}, thank you for loggin in again!")
else:
    print('We need to find some users!')