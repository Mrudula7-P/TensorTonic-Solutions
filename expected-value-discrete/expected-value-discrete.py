import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    n = len(x)
    prob = 0
    for i in range(n):
        prob += (x[i] * p[i])
    # Write code here
    return float(prob)
    pass