#Program to save to a file, the time in seconds of each short video.

def get_input():
    """Get the number of short videos from the user."""
    while True:
        try:
            number_of_videos = int(input('Enter the number of short '
                                         'videos: '))
            break
        except ValueError:
            print("Please enter a valid number of videos.")
    return number_of_videos

def write_to_file(file_path, number_of_videos):
    """Write the seconds of each file to a file."""
    #Open the file for writing.
    output = open(f'{file_path}', 'w')

    #Write the data to the file.
    for i in range(1, number_of_videos + 1):
        #Get input from the user.
        data = input(f'Enter the time for video #{i}: ')

        #Add the data to the file.
        output.write(data + '\n')

    #Close the file.
    output.close()

def main():
    """
    Mainline logic for writing the number of seconds of a video
    to a file.
    """
    file_path = 'files/video_times.txt'

    #Get the number of short videos.
    number_of_videos = get_input()

    #Write the seconds of each video to the file.
    write_to_file(file_path, number_of_videos)

#Call the main function.
if __name__ == '__main__':
    main()