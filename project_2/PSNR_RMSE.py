import numpy as np
import matplotlib.pyplot as plt
import os
def calculate_rmse_psnr(image1, image2, titles, names):
    # RMSE 
    output_dir = './project_2/image_output/Kernel_2/first_run'
    os.makedirs(output_dir, exist_ok=True)
    image1 = np.clip(image1, 0, 255).astype(np.float32)
    #print(f"Original{len(image1)}")
    image2 = np.clip(image2, 0, 255).astype(np.float32)

    diff = image1 - image2
    mse = np.mean(diff**2)
    rmse = np.sqrt(mse)
    
    # PSNR 
    max_pixel_value = 255  
    psnr = 20 * np.log10(max_pixel_value / rmse)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(image1, cmap='gray')
    axs[0].set_title("Original Image")
    axs[1].imshow(image2, cmap='gray')
    axs[1].set_title(f"{titles}")
    fig.suptitle(f'RMSE: {rmse:.2f} %, PSNR: {psnr:.2f} dB', fontsize=12, y=0.95)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, names))
    plt.show()
    
    return rmse, psnr
