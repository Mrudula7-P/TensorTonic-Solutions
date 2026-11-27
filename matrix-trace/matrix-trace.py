import numpy as np

def matrix_trace(A: list) -> float:
    total = 0
    A = np.array(A)
    for i in range(min(A.shape)):
        total += A[i, i]
    return float(total)
    pass