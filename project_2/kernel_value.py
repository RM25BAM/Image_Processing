import numpy as np
def kernel_value():
    print("Enter the kernel values row by row, separated by spaces \nFor example, for a 3x3 kernel, enter: '1 2 1' (press Enter), then '2 4 2' (press Enter), then '1 2 1' (press Enter).")
    kernel_rows = []
    for i in range(3):  
        row = input(f"Row {i + 1}: ")
        kernel_row = list(map(float, row.split()))
        kernel_rows.append(kernel_row)
    
    kernel = np.array(kernel_rows)
    
   
    kernel /= int(input("Kernal normalization: "))
    
    return kernel
