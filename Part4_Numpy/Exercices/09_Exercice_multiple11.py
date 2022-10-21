import numpy as np 

dataset = np.random.randint(1, 200, size=(20, 20))

# 1 
y11 = np.arange(11, 200, 11)
print(f'Liste de tous les multiples de 11 jusqu\'à 200 : \n {y11}')
print('--------------------------------------------------------------------------------------')

# 2 
mask = np.isin(dataset, y11) 
print(dataset[mask])
print('--------------------------------------------------------------------------------------')

# somme des multiples de 11 par ligne
print(f'Somme des multiples de 11 par ligne : \n {mask.sum(1)}')
print('--------------------------------------------------------------------------------------')

# 3 Supprimer les lignes qui ont au moins un multiple de 11
# Pour prendre la négation d'un masque on utilise l'opérateur binaire ~ 
mask_non11 = ~np.any(mask, axis=1)  # ~(au moins un multiple 11) = aucun multiple de 11

print(dataset[mask_non11])
print("-------")
print(dataset[np.any(mask, axis=1)])
