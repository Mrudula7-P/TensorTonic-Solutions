import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    n_samp, n_feat = X.shape
    w = np.zeros(n_feat, dtype = float)
    b = 0.0
    for _ in range(steps):
        z = X @ w + b
        y_pred = _sigmoid(z)

        error = y_pred - y
        dw = (1/ n_samp) * (X.T @ error)
        db = (1/ n_samp) * np.sum(error)

        w = w - lr * dw
        b = b - lr * db

    return w, float(b)
    pass