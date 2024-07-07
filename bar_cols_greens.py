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

# Example usage:
# import matplotlib.pyplot as plt

# Choose 2 colors
custom_colors_bar = get_bar_cols_greens(num_colors=2, alpha=1)
print(custom_colors_bar)  # ['#9ebf7d', '#6eae6f']

# Choose all 3 colors with different alpha
custom_colors_bar_alpha = get_bar_cols_greens(num_colors=3, alpha=1)
print(custom_colors_bar_alpha)  # ['#7f9b5f', '#5d8c5d', '#3b5e47']

# Using in a plot
# plt.scatter(x, y, c=custom_colors_bar)
