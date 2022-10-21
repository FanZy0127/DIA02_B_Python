import numpy as np


def circular(n):
    result = [[x if x <= n else x - n for x in range(i, n + i)] for i in range(1, n + 1)]
    return np.array(result)


print(circular(10))
