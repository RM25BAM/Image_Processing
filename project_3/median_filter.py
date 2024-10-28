"""
Undergraduate students 
A function utilizing median filtering without noise detection. The function shall accept a noisy 
image as a parameter and return a filtered image. Do not forget to take care of boundary effect 
and to extend an image over its boundaries using mirroring.
"""
import numpy as np

def median_filter(noisy_image):
    kernel_size = 3
    pad_size = 3 // 2
    # extend image through padding via reflect
    padded_image = np.pad(noisy_image, pad_size, mode='reflect')
    filtered_image = np.zeros_like(noisy_image)
    # Apply median filtering in the output image -> filtered
    for i in range(noisy_image.shape[0]):
        for j in range(noisy_image.shape[1]):
            region = padded_image[i:i + kernel_size, j:j + kernel_size]
            filtered_image[i, j] = np.median(region)
    return filtered_image