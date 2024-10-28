# comparsion display image of the noisy and the regular 
import matplotlib.pyplot as plt
import os
def comparison_display(img, noisy_img, type, corupt, rmse, psnr, figure_name):
    if type == "S":
        type = "Salt and Pepper"
    elif type == "R":
        type = "Random"
    output_dir = './project_3/image_output/comparsion_regular_noisy'
    os.makedirs(output_dir, exist_ok=True)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img, cmap='gray')
    axs[0].set_title("Original Image")
    axs[1].imshow(noisy_img, cmap='gray')
    axs[1].set_title(f"{type} Noisy Image")
    fig.suptitle(f'Coruption Rate {corupt:.2f}%,RMSE: {rmse:.2f} %, PSNR: {psnr:.2f} dB', fontsize=12, y=0.98)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, figure_name))
    plt.show()
