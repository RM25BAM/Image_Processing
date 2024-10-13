import smart_filter, GNAF, mean_filter, PSNR_RMSE, original_gaussian_display, original_mean_compare, reg_stat, kernel_value, original_smart_compare, spatial_domain_filtering, original_spatial_domain
from tabulate import tabulate

def analyze_image(img1): #
    # Q2 use a/b/c from Project 1 (mean + std)
    mean, std = reg_stat.reg_stats(img1)
    print("\nImage 1 statistics") # used library tabulate for pretty tables 
    table = [
        ["Mean", f"{mean}"],
        ["Standard Deviation", f"{std}"]
    ]
    print(tabulate(table, tablefmt="grid"))
    
    #Gaussian Noise Q1 B
    noise_fraction = float(input("\nInput the noise fraction for image: "))
    noisy_img = GNAF.GNAF(img1, noise_fraction)
    original_gaussian_display.original_gaussian_display(img1, noisy_img)
    
    # kernel values 
    kernel = kernel_value.kernel_value()

    # mean filtering Q1 C
    print("Mean Filter Image:\n Displaying...\n")
    mean_filtering = mean_filter.mean_filter(img1, kernel)
    original_mean_compare.mean_comparison(img1, mean_filtering)
    
    # smart filtering  Q1 C

    smart = smart_filter.smart_filter(img1, kernel)
    #display smart filter comparison with the reg - > making function 
    print("Smart Kerneling Filter Image:\n Displaying...\n")
    original_smart_compare.smart_comparison(img1 , smart)
    
    # spatial domain linear filtering EXTRA credit
    filter_img = spatial_domain_filtering.spatial_domain(img1, kernel)
    original_spatial_domain.spatial_comparison(img1, filter_img)



    #RMSE & PSNR 
    #noisy
    titles = ["RMSE & PSNR Noisy/Clean","RMSE & PSNR Mean Filter","RMSE & PSNR Smart Filter","RMSE & PSNR Spatial Domain"]
    variables = [noisy_img, mean_filtering, smart, filter_img]
    figure_name = ["figure5.png", "figure6.png", "figure7.png", "figure8.png"]
    for i in range(0,4):
        rmse, psnr = PSNR_RMSE.calculate_rmse_psnr(img1, variables[i], titles[i], figure_name[i])
        table = [
            [f"{titles[i]}"],
            ["RMSE", f"{rmse} %"],
            ["PSNR", f"{psnr} dB"]
        ]
        print(tabulate(table, tablefmt="grid"))
        print("\n")
"""     
    rmse, psnr = PSNR_RMSE.calculate_rmse_psnr(noisy_img, mean_filtering)
    table = [
        ["RMSE & PSNR Mean Filter"],
        ["RMSE", f"{rmse} %"],
        ["PSNR", f"{psnr} dB"]
    ]
    print(tabulate(table, tablefmt="grid"))
    print("\n")
    
    rmse, psnr = PSNR_RMSE.calculate_rmse_psnr(noisy_img, smart)
    table = [
        ["RMSE & PSNR Smart Filter"],
        ["RMSE", f"{rmse} %"],
        ["PSNR", f"{psnr} dB"]
    ]
    print(tabulate(table, tablefmt="grid"))
    print("\n")
    
    rmse, psnr = PSNR_RMSE.calculate_rmse_psnr(noisy_img, filter_img)
    table = [
        ["RMSE & PSNR Spatial Domain Filter"],
        ["RMSE", f"{rmse} %"],
        ["PSNR", f"{psnr} dB"]
    ]
    print(tabulate(table, tablefmt="grid")) """


    # need to do gaussian niose but any image (doesnt need to be clean)

    #for c lets apply linear filtering and desired kernel that person chose before and put the img before(with noise)

    # measure standard deviation + PSNR of noisy and clean and flitered and clean

    



    # based on RMSE and PSNR difference is higher. something wrong with the system