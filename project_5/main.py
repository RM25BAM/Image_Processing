import os
import cv2
import analyze_image
import numpy as np

def choose_files(directory):
    tiff_files = [f for f in os.listdir(directory) if f.endswith('.tif')]
    
    if not tiff_files:
        print("No TIFF files found in the directory.")
        return None, None
   
    print("Available TIFF files from Testing directory:")
    for idx, file in enumerate(tiff_files):
        print(f"{idx + 1}: {file}")

    file_choice_1 = int(input(f"Choose the first file (1-{len(tiff_files)}): ")) - 1
    if file_choice_1 < 0 or file_choice_1 >= len(tiff_files):
        print("Invalid choice for the first image. Exiting.")
        return None, None
    
    return os.path.join(directory, tiff_files[file_choice_1])

def process_tiff_files(directory):
    while True:
        file_path_1 = choose_files(directory)
        if file_path_1 is None:
            break  
        img = cv2.imread(file_path_1, cv2.IMREAD_GRAYSCALE)
        img = np.array(img)        
        if img is not None:
            print(f"Processing files: {file_path_1}")
            analyze_image.analyze_image(img)
        else:
            print(f"Failed to load one or both images: {file_path_1}")
        continue_choice = input("Do you want to process another pair of files? (Y/N): ").strip().upper()[0]
        if continue_choice != 'Y':
            break
directory = './Test_Images'
process_tiff_files(directory)