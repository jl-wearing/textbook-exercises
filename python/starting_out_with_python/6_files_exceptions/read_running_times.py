#Program to calculate the total running times and display them.

def calculate_total_video_time(file_path):
    """Sum the times for each video and return the total."""
    #Open the file for reading.
    try:
        infile = open(f"{file_path}", "r")
    except FileNotFoundError:
        print("File not found!")

    #Determine the total time in seconds.
    total_time = 0
    data = infile.readline()
    while data != '':
        #add the time to the total.
        total_time+= float(data)

        #get the next time.
        data = infile.readline()

    return total_time

def display_times(file_path):
    """Display the running times of each short video."""
    #Open the file for reading.
    try:
        infile = open(f"{file_path}", "r")
    except FileNotFoundError:
        print("File not found!")

    #Output
    i = 1
    for line in infile:
        print(f"Length of video #{i}: {line.rstrip('\n')} seconds.")
        i+=1

def main():
    """Mainline logic for displaying and calculating running times."""
    file_path = 'files/video_times.txt'

    #Display the time for each video.
    display_times(file_path)

    #Display the total running time.
    total_time = calculate_total_video_time(file_path)
    #Output
    print(f"\nTotal Video Time: {total_time:.1f} seconds.")

#Call the main function.
if __name__ == '__main__':
    main()