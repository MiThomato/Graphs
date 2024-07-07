def get_dp_cols_green_tan(alpha=1.0):
    """
    Returns a list of custom colors with alpha for use in plots.
    
    Args:
        alpha (float): The alpha value for the colors, ranging from 0 (transparent) to 1 (opaque).
    
    Returns:
        list: A list of RGBA color strings.
    """
    dp_cols_green_tan = [
        (85/255, 107/255, 47/255, alpha),  # darkolivegreen
        (128/255, 128/255, 128/255, alpha),  # grey
        (210/255, 180/255, 140/255, alpha)  # tan
    ]
    return dp_cols_green_tan

# Example usage:
# import matplotlib.pyplot as plt
# custom_colors_dp = get_dp_cols_green_tan(alpha=0.5)
# plt.scatter(x, y, c=custom_colors_dp)
