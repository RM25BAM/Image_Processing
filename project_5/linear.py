import numpy as np
def linear_combination(img, edged_image, alpha, k):
    # 0.85 * image + 0.15 * edged image
    combined = (alpha * img) + (k * edged_image)
    return np.clip(combined, 0, 255).astype(np.uint8)
