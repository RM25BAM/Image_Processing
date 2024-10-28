import numpy as np

def differential_rank_impulse_detector(image, r, s):
    # Calculate pad_width 
    pad_width = int(r // 2)  # Ensure pad_width is an integer
    print(f"Image shape: {image.shape}, r: {r}, pad_width: {pad_width}, type(pad_width): {type(pad_width)}")

    # extend the image using mirroring
    padded_image = np.pad(image, pad_width, mode='reflect')
    
    filtered_image = np.copy(image)
    
    # Apply differential rank impulse detection
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Extract the local window (rank interval)
            window = padded_image[i:i + r, j:j + r]
            center_pixel = image[i, j]
            
            # Calculate the difference between center pixel & surrounding pixels
            rank_diff = np.abs(window - center_pixel)
            rank_min = np.min(rank_diff)
            rank_max = np.max(rank_diff)
            
            # If rank difference exceeds threshold its noisy
            if rank_max - rank_min > s:
                # Apply median filtering to noisy pixel
                filtered_image[i, j] = np.median(window)
    
    return filtered_image
