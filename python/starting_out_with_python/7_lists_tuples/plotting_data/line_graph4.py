#Program to display a line graph for sales by year.
import matplotlib.pyplot as plt

def main():
    """Mainline logic for creating the line graph."""
    #X and Y coordinates for each point.
    x_coordinates = list(range(5))
    y_coordinates = [0, 3, 1, 5, 2]

    #Plot the coordinates on the graph.
    plt.plot(x_coordinates, y_coordinates, marker='o')

    #Set the title of the graph.
    plt.title("Sales by Year")

    #Set the x and y labels.
    plt.xlabel("Year")
    plt.ylabel("Sales")

    #Customize the tick marks.
    plt.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    #Add a grid.
    plt.grid(True)

    #Show the graph.
    plt.show()

#Call the main function.
if __name__ == '__main__':
    main()