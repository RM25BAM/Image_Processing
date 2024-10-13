from scipy.ndimage import convolve
import numpy as np
# Smart filter kernel
def smart_filter(image, kernel):
    image = np.clip(image, 0, 255).astype(np.float32)
   # Apply convolution using the given kernel
    filtered_image = convolve(image, kernel, mode='reflect')
    
    #print(f"I am the problem{len(filtered_image)}")
    return filtered_image


