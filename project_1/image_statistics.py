import numpy as ny

def image_statistics(image_array):
    # Flatten the image array to 1D for statistical calculation
    flat_image = image_array.flatten()
    
    # Calculate required statistics
    min_val = ny.min(flat_image) # min
    max_val = ny.max(flat_image) # max
    mean_val = ny.mean(flat_image) # mean
    std_val = ny.std(flat_image) #Standard Deviation
    variance_val = ny.var(flat_image)
    
    
    if std_val != 0:
        snr_val = mean_val / std_val
    else:
        snr_val = float('inf')  # SNR is infinite 
    
    return {
        "Min": min_val,
        "Max": max_val,
        "Mean": mean_val,
        "Standard Deviation": std_val,
        "Variance": variance_val,
        "SNR(Signal-to-Noise Ratio)": snr_val
    }
