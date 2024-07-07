### Example usage of custom colors for graphs

import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

## Step 1: Download the script from GitHub
url = 'https://raw.githubusercontent.com/MiThomato/graphs/main/dp_cols_green_tan.py'
r = requests.get(url)

with open('dp_cols_green_tan.py', 'w') as f:
    f.write(r.text)

# Step 2: Import the function
from dp_cols_green_tan import get_dp_cols_green_tan

def plot_mean_juiciness_with_datapoints(mean_juiciness, datapoints, categories, jitter=0.05):
    """
    Plots the mean juiciness for apples and oranges with individual datapoints.

    Args:
        mean_juiciness (dict): A dictionary with the mean juiciness for each fruit.
        datapoints (dict): A dictionary with individual datapoints for each fruit and category.
        categories (list): A list of categories for the datapoints.
        jitter (float): The amount of jitter to add to the datapoints for better visualization.
    """
    # Get the custom colors
    colors = get_dp_cols_green_tan(alpha=0.7)

    # Create the bar plot
    fig, ax = plt.subplots()
    palette = sns.color_palette('YlGn', 2)
    bar_positions = range(len(mean_juiciness))

    ax.bar(bar_positions, mean_juiciness.values(), color=palette, tick_label=mean_juiciness.keys())

    # Overlay the individual datapoints with jitter
    for i, (fruit, data) in enumerate(datapoints.items()):
        for j, category in enumerate(categories):
            y_values = data[category]
            x_values = np.random.normal(i, jitter, size=len(y_values))  # Add jitter to x-values
            ax.scatter(x_values, y_values, color=colors[j], label=category if i == 0 else "")

    # Add legend and labels
    ax.legend(title='Location')
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Juiciness')
    ax.set_title('Mean Juiciness for Apples vs Oranges with Individual Data Points')

    # Display the plot
    plt.show()

# Example data
mean_juiciness = {'Apples': 7, 'Oranges': 6}
datapoints = {
    'Apples': {
        'NY': [6, 7, 8, 7, 7, 8, 6, 9, 8, 7],
        'NJ': [5, 7, 9, 8, 6, 7, 5, 8, 6, 7],
        'DC': [6, 7, 8, 7, 8, 6, 7, 7, 6, 8]
    },
    'Oranges': {
        'NY': [5, 6, 7, 6, 6, 7, 5, 7, 6, 7],
        'NJ': [5, 6, 8, 6, 7, 6, 6, 7, 6, 8],
        'DC': [6, 6, 7, 7, 7, 6, 6, 7, 6, 7]
    }
}
categories = ['NY', 'NJ', 'DC']

# Plot the data with jitter
plot_mean_juiciness_with_datapoints(mean_juiciness, datapoints, categories, jitter=0.1)
