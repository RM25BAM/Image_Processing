import matplotlib.pyplot as plt
import os
def original_gaussian_display(img, noisy_img, figure_name='figure1.png'):
    output_dir = './project_2/image_output/Kernel_2/first_run'
    os.makedirs(output_dir, exist_ok=True)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img, cmap='gray')
    axs[0].set_title("Original Image")
    axs[1].imshow(noisy_img, cmap='gray')
    axs[1].set_title("Gaussian Noise Image")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, figure_name))
    plt.show()
