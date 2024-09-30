from matplotlib import pyplot as plt
import numpy as np


def linear_contrast_correction(img, target_mean, target_std):
    img_mean = np.mean(img)
    img_std = np.std(img)
    corrected_img = (img - img_mean) * (target_std / img_std) + target_mean
    corrected_img = np.clip(corrected_img, 0, 255).astype(np.uint8)
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(corrected_img, cmap='gray')
    plt.title('Contrast Corrected Image')
    plt.show()
    return corrected_img