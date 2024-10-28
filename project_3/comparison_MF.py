# comparsion display image of the noisy and the filter median and regular
import matplotlib.pyplot as plt
import os
def comparison_display(img, noisy, filtered_image, rmse, psnr, figure_name):
    output_dir = './project_3/image_output/comparison_median_filtering'
    os.makedirs(output_dir, exist_ok=True)
    fig, axs = plt.subplots(1, 3, figsize=(10, 5))
    axs[0].imshow(img, cmap='gray')
    axs[0].set_title("Original Image")
    axs[1].imshow(noisy, cmap='gray')
    axs[1].set_title("Noisy Image")
    axs[2].imshow(filtered_image, cmap='gray')
    axs[2].set_title("Median Filter Image")
    fig.suptitle(f'RMSE: {rmse:.2f} %, PSNR: {psnr:.2f} dB', fontsize=12, y=0.90)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, figure_name))
    plt.show()
