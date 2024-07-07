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

## Step 2: Import the function and create an example graph
from dp_cols_green_tan import get_dp_cols_green_tan

# Example data
fruits = ['Apple', 'Orange']
mean_juiciness = [6, 7]

# Individual datapoints for juiciness
apple_juiciness = [5, 6, 7, 6, 6]
orange_juiciness = [6, 7, 8, 7, 6]

# Custom colors for individual datapoints
colors = get_dp_cols_green_tan(alpha=0.5)

# Create the bar plot
palette = sns.color_palette('YlGn', 2)
fig, ax = plt.subplots()
bars = ax.bar(fruits, mean_juiciness, color=palette)

# Overlay the individual datapoints
x_positions = np.array([0, 1])  # x positions for the bars

# Jitter the datapoints around the bar positions for better visualization
jitter_amount = 0.05
x_jittered_apple = x_positions[0] + np.random.uniform(-jitter_amount, jitter_amount, len(apple_juiciness))
x_jittered_orange = x_positions[1] + np.random.uniform(-jitter_amount, jitter_amount, len(orange_juiciness))

ax.scatter(x_jittered_apple, apple_juiciness, color=colors[0], label='Apple datapoints')
ax.scatter(x_jittered_orange, orange_juiciness, color=colors[1], label='Orange datapoints')

# Adding labels and title
ax.set_xlabel('Fruits')
ax.set_ylabel('Juiciness (0-10)')
ax.set_title('Mean Juiciness of Apples and Oranges with Individual Datapoints')
ax.legend()

# Show plot
plt.show()
