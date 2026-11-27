import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    x = np.array(x)
    res = np.zeros_like(x, dtype=float)
    for i in range(len(x)):
        if x[i] == 0:
            res[i] = 1 - p
        else:
            res[i] = p

    return {"pmf" : res, "mean" : p, "variance" : p * (1 - p)}