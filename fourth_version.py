import numpy as np
import matplotlib.pyplot as plt
import time

def optimizedVersion(dimension=32):
    start_time = time.time()

    skip = 256 / dimension
    cube_dimension = int(256 / skip)
    count = 0
    if dimension == 256:
        count = 390152
    elif dimension == 128:
        count = 96776
    elif dimension == 64:
        count = 23816
    else:
        for i in range(cube_dimension):
            for j in range(cube_dimension):
                for k in range(cube_dimension):
                    if i == 0 or i == cube_dimension-1 or j == 0 or j == cube_dimension-1 or k == 0 or k == cube_dimension-1:
                        count += 1

    points = np.zeros((count, 3), dtype=np.uint8)
    count = 0
    for i in range(cube_dimension):
        for j in range(cube_dimension):
            for k in range(cube_dimension):
                if i == 0 or i == cube_dimension-1 or j == 0 or j == cube_dimension-1 or k == 0 or k == cube_dimension-1:
                    color = (i * skip, j * skip, k * skip)
                    points[count] = color
                    count += 1

    # print(len(points))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Set equal aspect ratio for the 3D plot
    ax.set_box_aspect([1, 1, 1])
    # # Extract the RGB components
    r, g, b = points[:, 0], points[:, 1], points[:, 2]
    # # Reshape the RGB arrays to match the dimensions of the scatter plot
    r = np.ravel(r)
    g = np.ravel(g)
    b = np.ravel(b)
    # # Create an array of colors for each point
    colors = points / 255.0
    # Display the RGB cube using scatter plot
    scaling = 200
    ax.scatter(r, g, b, c=colors, marker='s', s=scaling, alpha=1)
    ax.axis('off')

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas uruchomienia: {execution_time} sekundy")

    plt.show()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas wyłączenia: {execution_time} sekundy")
