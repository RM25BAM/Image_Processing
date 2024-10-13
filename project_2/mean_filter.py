import numpy as np
import cv2

def mean_filter(image, kernel):
    kernel = np.array(kernel, dtype=np.float32)
    kernel /= np.sum(kernel) 

 
    filtered_image = cv2.filter2D(image, -1, kernel.reshape((3, 3)))
    
    return filtered_image


""" fix """