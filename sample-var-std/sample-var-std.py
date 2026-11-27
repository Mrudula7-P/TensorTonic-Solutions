import numpy as np

def sample_var_std(x: list) -> dict:
    n = len(x) - 1
    if n < 1:
        return 
        
    x = np.array(x)
    mean = np.mean(x)
    
    var = np.sum((x - mean) ** 2) / n
    std = np.sqrt(var)
    return {"variance" : var, "standard_deviation" : std}
    pass