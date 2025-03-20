banned_users = ['andrew', 'carolina', 'david']
user = input('Enter your username: ')
if user.lower() not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')