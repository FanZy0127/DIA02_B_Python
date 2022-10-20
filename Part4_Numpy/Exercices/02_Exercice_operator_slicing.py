import numpy as np

y1 = np.array(
    [
        [5, 5, 1, 6, 5],
        [7, 7, 8, 9, 6],
        [1, 7, 2, 4, 5],
        [3, 4, 7, 0, 8],
        [1, 8, 2, 0, 2]
    ]
)

# 1. Multipliez les lignes paires par 2
# deep copy des opérateurs arithmétique pour créer une nouvelle matrice.
# np.array[start:end:step]
y_even = np.copy(y1)
y_even[::2, :] = y_even[::2, :] * 2
print(f'COPIE AVEC MULTIPLICATION DES LIGNES PAIRES PAR 2 : \n{y_even}')
print('--------------------------------------------------------------------------------------')

# 2. Multipliez une sur trois
y_thrice = np.copy(y1)
y_thrice[::3, :] = y_thrice[::3, :] * 3
print(f'COPIE AVEC MULTIPLICATION TOUTES LES 3 LIGNES PAR 3 : \n{y_thrice}')
print('--------------------------------------------------------------------------------------')

# 3. Ajoutez 100 à la dernière valeur de chaque ligne
y1[:, -1] = y1[:, -1] + 100
print(f'AJOUT DE 100 À LA VALEUR FINALE DE CHAQUE LIGNE : \n{y1}')
print('--------------------------------------------------------------------------------------')

# -------
y2 = np.array(
    [
        [
            [89, 26, 78, 55, 23],
            [32, 92, 86, 55, 27],
            [87, 46, 63, 43, 77],
            [27, 18, 15, 20, 65],
            [52, 75, 82,  9, 38]
        ],

        [
           [78, 20, 86, 16, 31],
            [46,  3, 59,  6, 50],
            [76, 73, 41, 66, 42],
            [70, 80, 62, 58, 41],
            [41, 65, 49,  0, 79]
        ],

        [
            [13,  9, 58, 35, 32],
            [80, 86, 30, 73, 18],
            [52, 73, 74,  8, 40],
            [80, 27, 26, 94,  8],
            [30, 62,  3, 35, 75]
        ],

        [
            [69, 54, 24, 28, 44],
            [29, 85, 56,  7, 69],
            [13,  1, 62, 10, 66],
            [6,  5, 31, 78, 92],
            [11, 41, 38,  4, 67]
        ],

        [
            [30, 91, 12, 10, 91],
            [65, 95, 36, 54, 35],
            [49, 96, 21,  5, 87],
            [68, 82, 90, 36, 56],
            [41, 18, 75, 39, 99]
        ]
    ]
)

# 4. Pour chaque ligne paire de chaque matrice paire, multipliez les valeurs par 2.
y2_first_copy = np.copy(y2)
y2_first_copy[::2, ::2, :] = y2_first_copy[::2, ::2, :] * 2
print(f'MULTIPLICATION PAR 2 POUR CHAQUE LIGNE PAIRE DE CHAQUE MATRICE PAIRE : \n{y2_first_copy}')
print('--------------------------------------------------------------------------------------')

# 5 Pour chaque matrice "impaire", en terme d'indice, ajoutez 100 aux valeurs.

y2_second_copy = np.copy(y2)
y2_second_copy[1::2] = y2_second_copy[1::2] + 100
print(f'AJOUT DE 100 AUX VALEURS DES MATRICES DONT L\'INDICE EST IMPAIR : \n{y2_second_copy}')
print('--------------------------------------------------------------------------------------')

"""
6 Reprenez la matrice initiale y2 et ajoutez 1000 à la dernière valeur de chaque ligne de chaque matrice.
"""

y2_third_copy = np.copy(y2)
y2_third_copy[:, :, -1] = y2_third_copy[:, :, -1] + 1000
print(f'AJOUT DE 1000 À LA VALEUR FINALE DE CHAQUE LIGNE DE CHAQUE MATRICE : \n{y2_third_copy}')
print('--------------------------------------------------------------------------------------')

"""
7. Pour chaque matrice "impaire", en terme d'indice, et dont la somme totale des valeurs est impaire, ajoutez 100 à 
toutes les valeurs de cette matrice.

Pour les valeurs impaires il n'y aucune matrice qui vérifie cette condition

"""

# matrices impaires
print(y2[1::2])
print(y2[1::2].sum(2))
print(y2[1::2].sum(2).sum(1))

mask = y2[1::2].sum(2).sum(1) % 2 != 0

print(mask)  # aucune matrice ne vérifie cette condition

# On travaille sur toutes les matrice
mask_all_matrix = y2.sum(2).sum(1) % 2 != 0
print(mask_all_matrix)

y2[mask_all_matrix] = y2[mask_all_matrix] + 100

print(y2)

