from matplotlib import pyplot as plt
import numpy as np


def plot_histogram(img):
    hist, bins = np.histogram(img.flatten(), bins=256, range=[0,256])
    plt.figure()
    plt.plot(hist)
    plt.title('Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    return hist