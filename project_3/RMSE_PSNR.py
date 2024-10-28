import numpy as np
import matplotlib.pyplot as plt
import os
def calculate_rmse_psnr(image1, image2):
    # RMSE 
    image1 = np.clip(image1, 0, 255).astype(np.float32)
    #print(f"Original{len(image1)}")
    image2 = np.clip(image2, 0, 255).astype(np.float32)
    diff = image1 - image2
    mse = np.mean(diff**2)
    rmse = np.sqrt(mse)
    
    # PSNR
    max_pixel_value = 255  
    psnr = 20 * np.log10(max_pixel_value / rmse)
    
    return rmse, psnr