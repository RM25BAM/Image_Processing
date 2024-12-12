import numpy as np
from matplotlib import pyplot as plt
def sobel_edge(img):
    if not isinstance(img, np.ndarray) or img.ndim != 2:
        raise ValueError("Input must be a 2D numpy array representing a grayscale image.")
    # Sobel kernels
    sobel_x = np.array([[-1, 0, 1], 
                        [-2, 0, 2], 
                        [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], 
                        [0, 0, 0], 
                        [1, 2, 1]])
    grad_x = np.zeros_like(img, dtype=float)
    grad_y = np.zeros_like(img, dtype=float)
    padded_image = np.pad(img, 1, mode='reflect')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded_image[i:i+3, j:j+3]
            grad_x[i, j] = np.sum(region * sobel_x)
            grad_y[i, j] = np.sum(region * sobel_y)
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    edged_image = np.clip(gradient_magnitude, 0, 255)
    return edged_image.astype(np.uint8)