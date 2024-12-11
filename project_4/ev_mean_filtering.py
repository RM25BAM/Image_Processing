import numpy as np
from scipy.ndimage import generic_filter
def rank_order_EV_filtering(noisy_img, window_size):
    stand = np.std(noisy_img)
    pad_size = window_size // 2 # mirroring
    padded_image = np.pad(noisy_img, pad_size, mode='reflect')
    filtered_image = np.zeros_like(noisy_img)
    for i in range(noisy_img.shape[0]): 
        for j in range(noisy_img.shape[1]):
            window = padded_image[i:i + window_size, j:j + window_size]
            flatten = window.flatten()
            central_pixel = noisy_img[i, j]
            ev_interval = [px for px in flatten if abs(px - central_pixel) <= stand]
            filtered_image[i, j] = np.mean(ev_interval) if ev_interval else central_pixel
    return filtered_image











""" import numpy as np
from scipy.ndimage import generic_filter

def rank_order_EV_filtering(img, window_size):
    pad_size = window_size // 2
    padded_image = np.pad(img, pad_size, mode='reflect')
    global_std_dev = np.std(img)
    ev_mean_filter = lambda window: np.mean(window) if np.std(window) <= global_std_dev else window[len(window) // 2]
    return generic_filter(padded_image, ev_mean_filter, size=window_size)[pad_size:-pad_size, pad_size:-pad_size]
 """