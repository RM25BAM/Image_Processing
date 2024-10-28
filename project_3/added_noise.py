import numpy as np
import analyze_image
import random

# Function to simulate impulse noise / salt and pepper
def simulate_impulse_noise(image, noise_type, corruption_rate):
    if noise_type not in ["R", "S"]:
        raise ValueError("Invalid noise type. Choose 'random' or 'salt-and-pepper'")
    noisy_image = np.copy(image)
    # dimension of img
    rows, cols = noisy_image.shape[:2]
    
    # cal number of pixels to corrupt based on the corruption rate
    num_corrupted_pixels = int(corruption_rate * rows * cols)
    
    # Corrupt pixels with salt-and-pepper noise
    if noise_type == "S":
        # Half of the corrupted pixels will be salt (255) and the other half pepper (0) 
        num_salt = num_corrupted_pixels // 2
        num_pepper = num_corrupted_pixels - num_salt

        # add salt noise
        for _ in range(num_salt):
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            noisy_image[x, y] = 255  # White pixel (salt)
        
        # Add pepper noise 
        for _ in range(num_pepper):
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            noisy_image[x, y] = 0  # Black pixel (pepper)
    
    # Corrupt pixels with random impulse noise 
    elif noise_type == "R":
        for _ in range(num_corrupted_pixels):
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            # Assign a random intensity value [0, 255]
            noisy_image[x, y] = random.randint(0, 255)
    
    return noisy_image




