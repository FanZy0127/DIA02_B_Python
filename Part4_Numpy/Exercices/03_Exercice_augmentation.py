import numpy as np

a = np.array([82, 92, 89, 65, 77, 66, 69, 65, 79, 51], dtype=np.float64)
rate = lambda x: x * 1.1

a = np.where(a % 2 == 0, rate(a), a)

print(a)

# Deuxième solution
b = np.array([82, 92, 89, 65, 77, 66, 69, 65, 79, 51], dtype=np.float64)
b[b % 2 == 0] = rate(b[b % 2 == 0])

print(b)
