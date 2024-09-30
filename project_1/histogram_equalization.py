import cv2
from matplotlib import pyplot as plt


def histogram_equalization(img):
    equalized_img = cv2.equalizeHist(img)
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title('Equalized Image')
    plt.show()
    return equalized_img