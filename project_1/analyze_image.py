import histogram_equalization, image_statistics, linear_contrast_correction, plot_histogram


def analyze_image(img, target_mean=128, target_std=64):
    print("Statistic info is on the terminal. Rest of the graphs you have to exit the current graph and the next graph will pop up!")
    print("Original Image Statistics: \n")                         #min max standard deviation variance SNR
    original_stats = image_statistics.image_statistics(img)
    print(original_stats)
    
    print("Original Image Histogram: ")
    plot_histogram.plot_histogram(img)
    # first two problems
    
    print("Histogram Equalization: ") 
    equalized_img = histogram_equalization.histogram_equalization(img)
    # extra credit
    print("Equalized Image Statistics: ")
    equalized_stats = image_statistics.image_statistics(equalized_img)
    print(equalized_stats)
    
    print("Equalized Image Histogram: ")
    plot_histogram.plot_histogram(equalized_img)

    # rest
    print("Performing Linear Contrast Correction... ")
    contrast_img = linear_contrast_correction.linear_contrast_correction(img, target_mean, target_std)
    
    print("Contrast Corrected Image Statistics: ")
    contrast_stats = image_statistics.image_statistics(contrast_img)
    print(contrast_stats)
    
    print("Contrast Corrected Image Histogram: ")
    plot_histogram.plot_histogram(contrast_img)
