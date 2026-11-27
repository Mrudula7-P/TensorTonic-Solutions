import numpy as np

def dot_product(x: list, y: list) -> float:
    x = np.array(x)
    y = np.array(y)
    total = np.sum(x * y)
    return float(total)
    pass