import numpy as np

def unsharp_masking(img, k):
    if not isinstance(img, np.ndarray) or img.ndim != 2:
        raise ValueError("Input must be a 2D numpy array representing a grayscale image.")
    smoothing_kernel = np.array([[-k/9, -k/9, -k/9],
                                  [-k/9, k+1-k/9, -k/9],
                                  [-k/9, -k/9, -k/9]])
    padded_image = np.pad(img, 1, mode='reflect')
    smoothed_image = np.zeros_like(img, dtype=float)
    for i in range(3):
        for j in range(3):
            smoothed_image += smoothing_kernel[i, j] * padded_image[i:i+img.shape[0], j:j+img.shape[1]]
            
    high_freq_detail = img - smoothed_image
    sharpened_image = img + k * high_freq_detail
    sharpened_image = np.clip(sharpened_image, 0, 255)
    return sharpened_image.astype(np.uint8)