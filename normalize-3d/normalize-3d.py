import numpy as np

def normalize_3d(v: list) -> np.ndarray:
    v = np.array(v, dtype = float)

    if v.ndim == 1:
        norm = np.sqrt(np.sum(v ** 2))
        if norm == 0:
            return v
        return v / norm

    else:
        norm = np.sqrt(np.sum(v ** 2, axis = 1, keepdims = True))
        norm[norm == 0] = 1
        return v / norm
        
    pass