import os
import cv2
import analyze_image 
import numpy as ny
def choose_file(directory):
    
    tiff_files = [f for f in os.listdir(directory) if f.endswith('.tif')]
    
    if not tiff_files:
        print("No TIFF files found in the directory.")
        return None
   
    print("Available TIFF files:")
    for idx, file in enumerate(tiff_files):
        print(f"{idx + 1}: {file}")
    
    file_choice = int(input(f"Choose a file (1-{len(tiff_files)}): ")) - 1
    
    if file_choice < 0 or file_choice >= len(tiff_files):
        print("Invalid choice. Exiting.")
        return None
    
    return os.path.join(directory, tiff_files[file_choice])

def process_tiff_files(directory):
    while True:
       
        file_path = choose_file(directory)
        
        if file_path is None:
            break  
        
        
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE) #sets to greyscale based on the image chosen 
        img = ny.array(img) # sets image into an array
        if img is not None:
            print(f"Processing file: {file_path}")
            
            analyze_image.analyze_image(img)
        else:
            print(f"Failed to load the image: {file_path}")
        
        # Ask if the user wants to process another file
        continue_choice = input("Do you want to process another file? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

# Example usage: Process TIFF files from a folder
directory = './Test_Images'
process_tiff_files(directory)
