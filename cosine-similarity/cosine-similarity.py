import numpy as np

def cosine_similarity(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    x = np.linalg.norm(a)
    y = np.linalg.norm(b)
    if x == 0 or y == 0:
        return 0.0
    return float(np.dot(a, b) / (x * y))