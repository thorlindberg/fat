from save_graph import save_graph
import matplotlib.pyplot as plt
import numpy as np

def plot_graph(title, weights, predictions, increases, decreases, days, labels, output):

    # Create a figure
    plot = plt.figure(figsize=(10, 5))

    # Plot the data points for weights
    plt.scatter(days, weights, label='Weight Data Points', color='blue')

    # Calculate the trend line for weights using numpy's polyfit
    z_weights = np.polyfit(days, weights, 1)
    p_weights = np.poly1d(z_weights)

    # Plot the trend line for weights
    plt.plot(days, p_weights(days), "--", label='Weight Trend Line', color='blue')

    # Plot the data points for predictions
    plt.scatter(days, predictions, label='Prediction Data Points', color='orange')

    # Calculate the trend line for predictions using numpy's polyfit
    z_predictions = np.polyfit(days, predictions, 1)
    p_predictions = np.poly1d(z_predictions)

    # Plot the trend line for predictions
    plt.plot(days, p_predictions(days), "--", label='Prediction Trend Line', color='orange')

    # Plot the data points for increases
    # plt.scatter(days, increases, label='Increase Data Points', color='red', marker='^')

    # Calculate the trend line for increases using numpy's polyfit
    z_increases = np.polyfit(days, increases, 1)
    p_increases = np.poly1d(z_increases)

    # Plot the trend line for increases
    plt.plot(days, p_increases(days), "--", label='Increase Trend Line', color='red')

    # Plot the data points for decreases
    # plt.scatter(days, decreases, label='Decrease Data Points', color='green', marker='v')

    # Calculate the trend line for decreases using numpy's polyfit
    z_decreases = np.polyfit(days, decreases, 1)
    p_decreases = np.poly1d(z_decreases)

    # Plot the trend line for decreases
    plt.plot(days, p_decreases(days), "--", label='Decrease Trend Line',  color='green')

    # Set plot title and labels
    plt.title(f'Day {title}')
    plt.ylabel(labels[0])
    plt.xlabel(labels[1])

    # Set grid and y-axis inversion
    plt.grid(axis='both')
    plt.yticks(range(min([int(n) for n in weights]) - 1, max([int(n) for n in weights]) + 1, 1))
    plt.xticks(range(min(days), max(days) + 1, 1))

    # Add legend
    plt.legend()

    # Save the graph
    save_graph(plot, output, title)