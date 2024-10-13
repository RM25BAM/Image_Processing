import matplotlib.pyplot as plt
import os
def smart_comparison(img , smart_filter, figure_name = 'figure3.png'):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    output_dir = './project_2/image_output/Kernel_2/first_run'
    os.makedirs(output_dir, exist_ok=True)
    axs[0].imshow(img, cmap='gray')
    axs[0].set_title("Original Image")
    axs[1].imshow(smart_filter, cmap='gray')
    axs[1].set_title(f"Smart Filtering Kernel Image")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, figure_name))
    plt.show()