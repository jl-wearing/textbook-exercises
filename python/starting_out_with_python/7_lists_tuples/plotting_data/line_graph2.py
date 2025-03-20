#Program to add more features to the plotted line graph.
import matplotlib.pyplot as plt

def main():
    """Mainline logic for displaying a line graph."""
    x_coordinates = list(range(5))
    y_coordinates = [0, 3, 1, 5, 2]

    #Create a graph.
    plt.plot(x_coordinates, y_coordinates)

    #Set the title of the line graph.
    plt.title("A simple line graph")

    #Set the x and y labels.
    plt.xlabel("X-coords")
    plt.ylabel("Y-coords")

    #Add a grid to the graph.
    plt.grid(True)

    #Show the plot.
    plt.show()

#Call the main function.
if __name__ == '__main__':
    main()