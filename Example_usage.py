##### Below are two examples for usage of custom colors for graphs; one for patapoints (dp) and one for bar graphs (bars).

#### Example usage of custom colors for overlaying individual datapoints:

### Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

### In case needed
## Step 0: Download the script from GitHub
#import requests
#url = 'https://raw.githubusercontent.com/MiThomato/Graphs/main/dp_cols_green_tan.py'
#r = requests.get(url)
#
#with open('dp_cols_green_tan.py', 'w') as f:
#    f.write(r.text)

### Part A - Step 1: Get custom colors
from dp_cols_green_tan import get_dp_cols_green_tan
colors = get_dp_cols_green_tan()

### Part B - Step 2: Generate example data
np.random.seed(0)
n_points = 20
apples_mean_juiciness = np.random.randint(0, 11, size=n_points)
oranges_mean_juiciness = np.random.randint(0, 11, size=n_points)
locations = ['NY', 'NJ', 'DC']
locations_data = np.random.choice(locations, size=n_points)

## Step 3: Create bar plots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Bar plot for apples
sns.barplot(x=locations_data, y=apples_mean_juiciness, palette=sns.color_palette('YlGn', 2), ax=axs[0])
axs[0].set_title('Mean Juiciness of Apples')
axs[0].set_xlabel('Locations')
axs[0].set_ylabel('Mean Juiciness (0-10)')

# Bar plot for oranges
sns.barplot(x=locations_data, y=oranges_mean_juiciness, palette=sns.color_palette('YlGn', 2), ax=axs[1])
axs[1].set_title('Mean Juiciness of Oranges')
axs[1].set_xlabel('Locations')
axs[1].set_ylabel('Mean Juiciness (0-10)')

## Step 4: Add individual datapoints with jitter
for i, loc in enumerate(locations):
    # Jitter x positions for better visualization
    x_jitter = np.random.normal(i, 0.1, size=n_points)
    
    # Scatter plot for apples
    axs[0].scatter(x_jitter[locations_data == loc], apples_mean_juiciness[locations_data == loc],
                   color=colors[i], label=f'{loc} Apples', alpha=0.7)
    
    # Scatter plot for oranges
    axs[1].scatter(x_jitter[locations_data == loc], oranges_mean_juiciness[locations_data == loc],
                   color=colors[i], label=f'{loc} Oranges', alpha=0.7)

## Step 5: Finalize and show the plot
fig.tight_layout()
plt.suptitle('Mean Juiciness and Individual Datapoints of Apples and Oranges')
plt.legend(loc='upper right')
plt.show()



def get_bar_cols_greens(num_colors=3, alpha=1.0):
    """
    Returns a list of custom colors with alpha for use in plots.

    Args:
        num_colors (int): Number of colors to return, can be 1, 2, or 3.
        alpha (float): The alpha value for the colors, ranging from 0 (transparent) to 1 (opaque).

    Returns:
        list: A list of RGBA color strings.
    """
    bar_cols_greens = [
        f"#{int(155 * alpha + (1 - alpha) * 255):02x}{int(191 * alpha + (1 - alpha) * 255):02x}{int(125 * alpha + (1 - alpha) * 255):02x}",
        f"#{int(111 * alpha + (1 - alpha) * 255):02x}{int(174 * alpha + (1 - alpha) * 255):02x}{int(111 * alpha + (1 - alpha) * 255):02x}",
        f"#{int(46 * alpha + (1 - alpha) * 255):02x}{int(119 * alpha + (1 - alpha) * 255):02x}{int(71 * alpha + (1 - alpha) * 255):02x}"
    ]
    
    if num_colors == 1:
        colors = [bar_cols_greens[0]]
    elif num_colors == 2:
        colors = [bar_cols_greens[0], bar_cols_greens[1]]
    elif num_colors == 3:
        colors = bar_cols_greens
    else:
        raise ValueError("num_colors must be 1, 2, or 3.")
    
    return colors
   
print(f"The get_bar_cols_greens function now includes a num_colors parameter which determines how many colors to return.\n"
      f"Depending on the value of num_colors, the function returns a sublist of bar_cols_greens containing 1, 2, or 3 colors.")



######################################################################



#### Example usage of bar colors equivalent to Seaborn's YlGn palette:

## Example usage:
import matplotlib.pyplot as plt
import numpy as np

# Define sample data
categories = ['Category 1', 'Category 2', 'Category 3']
values = np.random.randint(1, 10, size=len(categories))
colors = get_bar_cols_greens(num_colors=3, alpha=0.9)  

# Plotting
plt.figure(figsize=(8, 6))
bars = plt.bar(categories, values, color=colors)

# Add labels, title, and grid
plt.title('Bar Plot with Custom Colors')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
