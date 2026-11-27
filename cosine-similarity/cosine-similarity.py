import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a = np.array(a)
    b = np.array(b)
    prod = np.dot(a, b)
    norm1 = np.linalg.norm(a)
    norm2 = np.linalg.norm(b)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return prod /(norm1 * norm2)
    pass