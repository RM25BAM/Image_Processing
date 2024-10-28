import added_noise, comparison_NR, differential, comparison_DR, median_filter, comparison_MF, RMSE_PSNR
from tabulate import tabulate
def analyze_image(img1):
    count  = 1
    # noise
    noise_images = []
    while True:
        noise = input("What type of noise salt and pepper(S) or random(R) or skip(Q): ")[0]
        noise = noise.upper()
        if noise == 'Q':
            break
        corruption_rate = float(input("What is the coruption rate: "))
        noisy_img = added_noise.simulate_impulse_noise(img1, noise, corruption_rate)
        noise_images.append(noisy_img)
        rmse, psnr = RMSE_PSNR.calculate_rmse_psnr(img1, noisy_img)
        # make tables for the rsme and psnr
        table = [
            [f"Added Noise {noise}"],
            ["RMSE", f"{rmse} %"],
            ["PSNR", f"{psnr} dB"]
            ]
        print(tabulate(table, tablefmt="grid"))
        print("\n")
        comparison_NR.comparison_display(img1, noisy_img, noise, corruption_rate, rmse, psnr, figure_name=f'figure{count}.png')
        count += 1
    for index, noisy in enumerate(noise_images):
        r = int(input("Enter the rank length: "))
        s = int(input("Enter the intensity difference: "))
        filtered_image = differential.differential_rank_impulse_detector(noisy, r, s)
        rmse, psnr = RMSE_PSNR.calculate_rmse_psnr(noisy, filtered_image)
        table = [
        ["Differential Rank Impulse Detector"],
        ["RMSE", f"{rmse} %"],
        ["PSNR", f"{psnr} dB"]
        ]
        print(tabulate(table, tablefmt="grid"))
        print("\n")
        comparison_DR.comparison_display_DRID(img1, noisy, filtered_image, rmse, psnr, figure_name=f'figure{index}.png')
        # for the median filter
        filter_image = median_filter.median_filter(noisy_img)
        rmse, psnr = RMSE_PSNR.calculate_rmse_psnr(noisy, filter_image)
        # make tables for the rsme and psnr
        table = [
        ["Mean Filter"],
        ["RMSE", f"{rmse} %"],
        ["PSNR", f"{psnr} dB"]
        ]
        print(tabulate(table, tablefmt="grid"))
        print("\n")
        comparison_MF.comparison_display(img1, noisy, filtered_image, rmse, psnr, figure_name=f'figure{index}.png')
            
