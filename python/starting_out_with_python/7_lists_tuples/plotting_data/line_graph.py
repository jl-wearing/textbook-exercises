#Program to display a simple line graph.
import matplotlib.pyplot as plt

def main():
    """Mainline logic for displaying a line graph."""
    x_coordinates = list(range(5))
    y_coordinates = [0, 3, 1, 5, 2]

    #Create a graph using the plot() method.
    plt.plot(x_coordinates, y_coordinates)

    #Show the graph.
    plt.show()

#Call the main function.
if __name__ == '__main__':
    main()