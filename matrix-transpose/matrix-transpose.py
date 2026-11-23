import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    row = len(A)
    col = len(A[0])

    B = np.zeros((col, row), dtype = np.array(A).dtype)
    for i in range(col):
        for j in range(row):
            B[i][j] = A[j][i]
    return B
    # Write code here
    pass
