from return_values import get_formatted_name

prompt = "enter name: "
prompt+= "\nor enter 'q' to quit: "

while True:
    #Input first name
    f_name = input(prompt)

    if f_name == 'q':
        break

    #Input last name.
    l_name = input(prompt)

    if l_name == 'q':
        break

    #Display information about user.
    user = get_formatted_name(f_name, l_name)
    print(f"Hello, {user}!")