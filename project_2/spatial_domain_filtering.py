import mirror_image
import numpy as np
def spatial_domain(img, kernel):
# Mirror the image
    mirrored_image = mirror_image.mirror_image(img)

    # Get the dimensions of the image
    image_height, image_width = img.shape
    
    # Create an output image with the same dimensions as the input image
    filtered_image = np.zeros_like(img)

    # Perform the filtering
    for i in range(image_height):
        for j in range(image_width):
            # Extract the 3x3 neighborhood
            neighborhood = mirrored_image[i:i+3, j:j+3]
            # Apply the kernel to the neighborhood
            filtered_value = np.sum(neighborhood * kernel)
            # Assign the filtered value to the output image
            filtered_image[i, j] = filtered_value

    return filtered_image