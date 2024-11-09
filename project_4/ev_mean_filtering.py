import numpy as np
from scipy.ndimage import generic_filter
def rank_order_EV_filtering(noisy_img, window_size):
    global_std_dev = np.std(noisy_img)  
    def adaptive_ev_filter(window):
        local_std_dev = np.std(window)
        local_mean = np.mean(window)
        central_pixel = window[len(window) // 2]
        weight = min(1, global_std_dev / (local_std_dev + 1e-5))  
        return (weight * local_mean) + ((1 - weight) * central_pixel)
    pad_size = window_size // 2
    padded_image = np.pad(noisy_img, pad_size, mode='reflect')
    filtered_img = generic_filter(padded_image, adaptive_ev_filter, size=window_size)
    filtered_img = filtered_img[pad_size:-pad_size, pad_size:-pad_size]  
    return filtered_img









""" import numpy as np
from scipy.ndimage import generic_filter

def rank_order_EV_filtering(img, window_size):
    pad_size = window_size // 2
    padded_image = np.pad(img, pad_size, mode='reflect')
    global_std_dev = np.std(img)
    ev_mean_filter = lambda window: np.mean(window) if np.std(window) <= global_std_dev else window[len(window) // 2]
    return generic_filter(padded_image, ev_mean_filter, size=window_size)[pad_size:-pad_size, pad_size:-pad_size]
 """