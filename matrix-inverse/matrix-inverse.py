import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    A = np.array(A, dtype = float)
    n = A.shape[0]
    # augmentation of the matrix
    aug = np.hstack((A, np.eye(n)))

    for i in range(n):
        pivot = i + np.argmax(np.abs(aug[i:, i]))

        aug[[i, pivot]] = aug[[pivot, i]]

        if abs(aug[i, i]) < 1e-10:
            return None

        aug[i] = aug[i] / aug[i, i]

        for j in range(n):
            if i != j:
                aug[j] = aug[j] - aug[i] * aug[j, i]
    
    return aug[:, n:]