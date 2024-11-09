# comparsion display image of the noisy and the regular 
import matplotlib.pyplot as plt
import os
def comparison_display(img, noisy_img, filter_img, rmse, psnr, figure_name):
    output_dir = './project_4/image_output'
    os.makedirs(output_dir, exist_ok=True)
    fig, axs = plt.subplots(1, 3, figsize=(10, 5))
    axs[0].imshow(img, cmap='gray')
    axs[0].set_title("Original Image")
    axs[1].imshow(noisy_img, cmap='gray')
    axs[1].set_title("Noisy Image")
    axs[2].imshow(noisy_img, cmap='gray')
    axs[2].set_title("Filtered Image")
    fig.suptitle(f'RMSE: {rmse:.2f} %, PSNR: {psnr:.2f} dB', fontsize=12, y=0.95)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, figure_name))