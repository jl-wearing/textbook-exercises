#Program to display a simple pie chart.
import matplotlib.pyplot as plt

def main():
    """Mainline logic for drawing a simple pie chart."""
    # Create a list of values.
    values = [20, 60, 80, 40]

    # Create labels for each slice.
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

    # Create a pie chart from the values.
    plt.pie(values, labels=slice_labels)

    # Set a title.
    plt.title("Sales by Qtr")

    # Display the chart.
    plt.show()

#Call the main function.
if __name__ == '__main__':
    main()