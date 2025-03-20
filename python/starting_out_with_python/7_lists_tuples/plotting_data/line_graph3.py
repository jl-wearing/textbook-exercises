#Program to add more features to the plotted line graph.
import matplotlib.pyplot as plt

def main():
    """Mainline logic for plotting line graphs."""
    x_coordinates = list(range(5))
    y_coordinates = [0, 3, 1, 5, 2]

    #Create a line graph.
    plt.plot(x_coordinates, y_coordinates)

    #Add a title.
    plt.title("Interesting Title")

    #Set the x and y labels.
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    #Make the grid visible.
    plt.grid(True)

    #Set the x and y axes limits.
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)

    #Show the graph.
    plt.show()

#Call the main function.
if __name__ == '__main__':
    main()