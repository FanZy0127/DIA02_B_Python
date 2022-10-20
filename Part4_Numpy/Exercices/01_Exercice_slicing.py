import numpy as np

x1 = np.array(
    [
        [9, 1, 2],
        [8, 0, 2],
        [5, 1, 5]
    ]
)

# 1 première ligne
print(x1[0, :])

# 2 deuxième colonne
print(x1[:, 1])

# 3 somme lignes et colonnes
print(x1.sum(1))  # lignes
print(x1.sum(0))  # colonnes

# 4 Destructuration somme des colonnes
(c1, c2, c3) = x1.sum(0)
print((c1, c2, c3))

# 5 Destructuration somme des lignes
(l1, l2, l3) = x1.sum(1)
print((l1, l2, l3))

# Dimension 2x2x2
x2 = np.array(
    [
        [
            [8, 4],
            [8, 9]
        ],
        [
            [3, 0],
            [5, 0]
        ]
    ]
)

# 6 somme axis = 0
print(x2.sum(0))

# 7 somme axis = 1
print(f'Somme axe 1 du tableau x2 : {x2.sum(1)}')

# 8 somme axis = 2
print(f'Somme axe 2 du tableau x2 : {x2.sum(2)}')

# 9 tableau de dimension 1X2 somme total de chaque ligne
x3 = x2.sum(2).sum(1)
print(f'x3 : {x3}')

# Sélection
print(x2[:, :, 1])

"""
array([[4, 9],
       [0, 0]])

"""
