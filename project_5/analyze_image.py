import numpy as np
from tabulate import tabulate
import cv2
import sobel, linear, unsharp
from matplotlib import pyplot as plt
import plot
import rmse_mse

def analyze_image(img):
    edged_image = sobel.sobel_edge(img)
    k = float(input("Enter k: "))
    sharpened_image = unsharp.unsharp_masking(img, k)
    alpha = float(input("Enter alpha: "))
    combined_image = linear.linear_combination(img, edged_image, alpha, 0.15)
    rmse_edged, mse_edged = rmse_mse.rmse_mse(img, edged_image)
    rmse_sharpened, mse_sharpened = rmse_mse.rmse_mse(img, sharpened_image)
    rmse_combined, mse_combined = rmse_mse.rmse_mse(img, combined_image)
    headers = ["Transformation", "RMSE", "MSE"]
    data = [
        ["Edge Detection", f"{rmse_edged:.4f}", f"{mse_edged:.4f}"],
        ["Unsharp Masking", f"{rmse_sharpened:.4f}", f"{mse_sharpened:.4f}"],
        ["Linear Combination", f"{rmse_combined:.4f}", f"{mse_combined:.4f}"]
    ]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    plot.plot(img, edged_image, sharpened_image, combined_image, figure_name="output")
