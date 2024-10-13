import numpy as np
def GNAF(clean_image, noise_fraction):
    image_std = np.std(clean_image)
    noise_std = noise_fraction * image_std
    noise = np.random.normal(0, noise_std, clean_image.shape) # 0 mean, niose std user chooses , then the image.shape to apply the noise
    noisy_image = clean_image + noise
    return noisy_image

"""
This procedure for generation of additive Gaussian noise is
equivalent to generation of a 2-D field of random numbers
with Gaussian (normal) distribution, with zero mean and
standard deviation σn equal to 0.1 to 0.5 of the clear image.
• Then this noise shall be added to the clear image component-
wise
"""