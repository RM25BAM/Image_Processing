import numpy as np
def rmse_mse(original, processed):
    mse = np.mean((original - processed) ** 2)
    rmse = np.sqrt(mse)
    return rmse, mse