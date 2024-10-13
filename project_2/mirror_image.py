import numpy as np
# this section i needed help from a program to take the matlab and convert eqivalent to python
def mirror_image(image):
    rows, cols = image.shape

    # Create a new image with extended dimensions
    mirrored = np.zeros((rows + 2, cols + 2), dtype=image.dtype)

    # Fill the center with the original image
    mirrored[1:rows + 1, 1:cols + 1] = image

    # Fill the edges by mirroring
    mirrored[0, 1:cols + 1] = mirrored[1, 1:cols + 1]  # Top
    mirrored[rows + 1, 1:cols + 1] = mirrored[rows, 1:cols + 1]  # Bottom
    mirrored[1:rows + 1, 0] = mirrored[1:rows + 1, 1]  # Left
    mirrored[1:rows + 1, cols + 1] = mirrored[1:rows + 1, cols]  # Right

    # Fill corners
    mirrored[0, 0] = mirrored[1, 1]  # Top-left
    mirrored[0, cols + 1] = mirrored[1, cols]  # Top-right
    mirrored[rows + 1, 0] = mirrored[rows, 1]  # Bottom-left
    mirrored[rows + 1, cols + 1] = mirrored[rows, cols]  # Bottom-right

    return mirrored
