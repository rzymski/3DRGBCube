import numpy as np
import matplotlib.pyplot as plt

def slow_version():
    # Full 8-bit RGB space
    bits = 8
    cube_dimension = 2 ** bits
    full_rgb_space = np.zeros((cube_dimension, cube_dimension, cube_dimension, 3), dtype=np.uint8)

    # Fill the 3D RGB cube
    for i in range(cube_dimension):
        for j in range(cube_dimension):
            for k in range(cube_dimension):
                color = (i, j, k)
                full_rgb_space[i, j, k] = color

    # Create a figure and 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # # Extract the RGB components
    r, g, b = full_rgb_space[:, :, :, 0], full_rgb_space[:, :, :, 1], full_rgb_space[:, :, :, 2]
    #
    # # Reshape the RGB arrays to match the dimensions of the scatter plot
    r = r.flatten()
    g = g.flatten()
    b = b.flatten()
    #
    # # Create an array of colors for each point
    colors = full_rgb_space / 255.0
    colors = colors.reshape(-1, 3)
    #
    # # Display the RGB cube using scatter plot
    ax.scatter(r, g, b, c=colors, marker='s')

    ax.axis('off')
    plt.show()