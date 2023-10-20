import numpy as np
import matplotlib.pyplot as plt
import time

def slow_version():
    start_time = time.time()

    skip = 8
    cube_dimension = int(256 / skip)
    full_rgb_space = np.zeros((cube_dimension, cube_dimension, cube_dimension, 3), dtype=np.uint8)
    # Fill the 3D RGB cube
    for i in range(cube_dimension):
        for j in range(cube_dimension):
            for k in range(cube_dimension):
                color = (i * skip, j * skip, k * skip)
                full_rgb_space[i, j, k] = color
    # Create a figure and 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # # Extract the RGB components
    r, g, b = full_rgb_space[:, :, :, 0], full_rgb_space[:, :, :, 1], full_rgb_space[:, :, :, 2]
    # # Reshape the RGB arrays to match the dimensions of the scatter plot
    r = np.ravel(r)
    g = np.ravel(g)
    b = np.ravel(b)
    # # Create an array of colors for each point
    colors = full_rgb_space / 255.0
    colors = colors.reshape(-1, 3)
    # Display the RGB cube using scatter plot
    scaling = 200
    ax.scatter(r, g, b, c=colors, marker='s', s=scaling)
    # without scaling
    # ax.scatter(r, g, b, c=colors, marker='s')
    ax.axis('off')

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas wykonania funkcji: {execution_time} sekundy")

    plt.show()


