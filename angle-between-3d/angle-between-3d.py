import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    num = np.dot(v, w)
    ss_v = 0
    for i in v:
        ss_v += i * i
    ss_v = ss_v ** 0.5

    ss_w = 0
    for i in w:
        ss_w += i * i
    ss_w = ss_w ** 0.5
    theta = np.clip(num/(ss_v * ss_w), -1.0, 1.0)
    val = np.arccos(theta)
    return val
    pass