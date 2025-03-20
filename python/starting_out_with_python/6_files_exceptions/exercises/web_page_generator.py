#Program to create a simple web page for a user.

def main():
    """Mainline logic for creating web pages."""
    #Get information about a user.
    name = input('Enter your name: ')
    description = input('Describe yourself: ')

    #Create an HTML file about the user.
    try:
        #Open the file for writing.
        output = open('files/user.html', 'w')

        #Add html information.
        output.write('<html>')
        output.write('<head>')
        output.write('</head>')
        output.write('<body>')
        output.write('<center>')
        output.write(f'<h1>{name.title()}</h1>')
        output.write('</center>\n')
        output.write('<hr />\n')
        output.write(f'{description}\n')
        output.write('<hr />\n')
        output.write('</body>\n')
        output.write('</html>\n')

        #Close the file.
        output.close()
    except Exception as err:
        print(f"An error has occurred: {err}")

#Call the main function.
if __name__ == '__main__':
    main()