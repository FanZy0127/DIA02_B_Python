import numpy as np

A = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 10, 69, 12],
])

min_index = zip(A.argmin(1), A.min(1))

for (min_val, index) in min_index:
    print(min_val, index)

print(list(zip(A.argmin(1), A.min(1))))

min_index = np.array(list(zip(A.argmin(1), A.min(1))))
print(f'MIN_INDEX : \n {min_index}')


"""
SOLUTIONS ANNEXES
"""
# 1
minTabLine = [(int(np.where(row == min(row))[0]), min(row)) for row in A]
print(minTabLine)
# OU
minTabLine2 = [(int(np.where(row == np.amin(row))[0]), np.amin(row)) for row in A]
print(minTabLine2)

# 2


def min_tab_ine(l):
    return [(np.argmin(a), np.amin(a)) for a in l]


print(f'MIN_INDEX RETURNED BY FUNCTION : {min_tab_ine(A)}')

