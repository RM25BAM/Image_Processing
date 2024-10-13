import numpy as np
def reg_stats(img):
    flat_image = img.flatten()
    mean_val = np.mean(flat_image) # mean
    std_val = np.std(flat_image) #Standard Deviation
    return mean_val, std_val