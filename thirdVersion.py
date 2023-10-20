import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # Import Poly3DCollection
import time

def edges_version(dimension=32):
    start_time = time.time()

    # Create a 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def createSquaresAndColorsForSide(dimension, startX, startY, startZ, direction=None):
        squares = []
        colors = []
        if direction == "xz":  # przod i tyl
            for x in range(startX, dimension-1):
                for z in range(startZ, dimension-1):
                    square = [[x, startY, z], [x+1, startY, z], [x+1, startY, z+1], [x, startY, z+1]]
                    squares.append(square)
                    color = (x / dimension, startY / dimension, z / dimension, 1)
                    colors.append(color)
        elif direction == "xy":  # dol i gora
            for x in range(startX, dimension-1):
                for y in range(startY, dimension-1):
                    square = [[x, y, startZ], [x+1, y, startZ], [x+1, y+1, startZ], [x, y+1, startZ]]
                    squares.append(square)
                    color = (x / dimension, y / dimension, startZ / dimension, 1)
                    colors.append(color)
        elif direction == "yz":  # lewo i prawo
            for y in range(startY, dimension-1):
                for z in range(startZ, dimension-1):
                    square = [[startX, y, z], [startX, y+1, z], [startX, y+1, z+1], [startX, y, z+1]]
                    squares.append(square)
                    color = (startX / dimension, y / dimension, z / dimension, 1)
                    colors.append(color)
        else:
            raise Exception("Wrong parameters. Wrong direction. Should be 'xz', 'xy' or 'yz'")
        return squares, colors

    squares1, colors1 = createSquaresAndColorsForSide(dimension, 0, 0, 0, "xz")  # przod
    squares2, colors2 = createSquaresAndColorsForSide(dimension, dimension-1, 0, 0, "yz")  # prawo
    squares3, colors3 = createSquaresAndColorsForSide(dimension, 0, dimension-1, 0, "xz")  # tyl
    squares4, colors4 = createSquaresAndColorsForSide(dimension, 0, 0, 0, "yz")  # lewo
    squares5, colors5 = createSquaresAndColorsForSide(dimension, 0, 0, dimension-1, "xy")  # gora
    squares6, colors6 = createSquaresAndColorsForSide(dimension, 0, 0, 0, "xy")  # dol

    # print(squares1)
    squares = squares1 + squares2 + squares3 + squares4 + squares5 + squares6
    colors = colors1 + colors2 + colors3 + colors4 + colors5 + colors6


    for i in range(len(squares)):
        ax.add_collection3d(Poly3DCollection([squares[i]], facecolors=[colors[i]], edgecolors=[colors[i]]))

    # Set the aspect ratio to be equal
    ax.set_box_aspect([dimension-1, dimension-1, dimension-1])

    # Set labels for the axes
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')

    # Set the limits for the axes
    ax.set_xlim(0, dimension-1)
    ax.set_ylim(0, dimension-1)
    ax.set_zlim(0, dimension-1)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas wykonania funkcji: {execution_time} sekundy")

    ax.axis('off')
    plt.show()


