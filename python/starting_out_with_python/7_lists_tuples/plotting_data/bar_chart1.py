#Program to create a simple bar chart.
import matplotlib.pyplot as plt

def main():
    """Mainline logic for displaying bar charts."""
    # Create a list with the x-coordinate's of each bar's left edge.
    left_edges = list(range(0, 41, 10))

    # Create a list with the heights of each bar.
    heights = list(range(100, 501, 100))

    # Create a bar chart.
    bar_width = 10
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'k', 'y'))

    #

    # Add a title to the bar chart.
    plt.title("Sales by Year")

    # Set the tick names of each axis.
    plt.xticks([0, 10, 20, 30, 40], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([100, 200, 300, 400, 500], ['$1m', '$2m', '$3m', '$4m', '$5m'])

    # Add labels to the axes.
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Add a grid to the chart.
    plt.grid(True)

    # Show the chart.
    plt.show()

#Call the main function.
if __name__ == '__main__':
    main()