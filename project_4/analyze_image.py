import numpy as np, ev_mean_filtering, GNAF, comparison_noisy_ev
from tabulate import tabulate
def analyze_image(img):
    noise_fraction = float(input("\nInput the noise fraction for image: "))
    noisy_img = GNAF.GNAF(img, noise_fraction)
    while True:
        window_size = int(input("Input the window size: "))
        if window_size % 2 == 0:
            raise ValueError("Window size must be an odd integer [3,5,7].")
            continue
        else:
            break
    filtered_img = ev_mean_filtering.rank_order_EV_filtering(noisy_img, window_size)
    diff = img - filtered_img
    mse = np.mean(diff**2)
    rmse = np.sqrt(mse)
    max_pixel_value = 255  
    psnr = 20 * np.log10(max_pixel_value / rmse)
    table = [
            [f"Original v. Filtered"],
            ["RMSE", f"{rmse} %"],
            ["PSNR", f"{psnr} dB"]
            ]
    print(tabulate(table, tablefmt="grid"))
    print("\n")
    comparison_noisy_ev.comparison_display(img, noisy_img, filtered_img, rmse, psnr, figure_name="comparison")

