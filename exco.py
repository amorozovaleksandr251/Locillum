import numpy as np

# Define the transformation function
def transform(x, y, angle):
    # Convert angle to radians
    angle_rad = np.deg2rad(angle)
    
    # Perform transformation
    x_new = x * np.cos(angle_rad) - y * np.sin(angle_rad)
    y_new = x * np.sin(angle_rad) + y * np.cos(angle_rad)
    
    return x_new, y_new

# Test the transformation function
x, y = 3, 4
angle = 45  # in degrees
x_new, y_new = transform(x, y, angle)
print(f'Original point: ({x}, {y})')
print(f'Transformed point: ({x_new}, {y_new})')
