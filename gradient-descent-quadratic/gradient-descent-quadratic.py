def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    x = float(x0)
    for _ in range(steps):
        grad = 2 * a * x0 + b
        x = x0 - lr * grad
        x0 = x
    return x
    pass