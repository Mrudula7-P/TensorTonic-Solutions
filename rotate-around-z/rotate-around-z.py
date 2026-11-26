import numpy as np

def rotate_around_z(points: list, theta: float) -> np.ndarray:
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    
    if isinstance(points[0], (int, float, np.number)):
        res = np.zeros(3)
        res[0] = points[0] * cos_t - points[1] * sin_t
        res[1] = points[0] * sin_t + points[1] * cos_t
        res[2] = points[2]
        return res
        
    n = len(points)
    res = np.zeros((n, 3))
    
    for i in range(n):
        res[i][0] = points[i][0] * cos_t - points[i][1] * sin_t
        res[i][1] = points[i][0] * sin_t + points[i][1] * cos_t
        res[i][2] = points[i][2]
    return res
    pass