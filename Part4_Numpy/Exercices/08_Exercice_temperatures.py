import numpy as np 

january = np.array(
      [-2, 5, -5, 6, -2, 0, 6, 2, 8, 0, 6, -1, 3, 3, 7, 0, -5, 7, 4, 7, 8, -1, 5, -2, 3, -3, -2, 7, 8, 4, 2]
)

# 1 températures supérieures à 0
print(f'1) Températures supérieueres à 0° sur le mois de Janvier : \n {january[january > 0]}')
print('--------------------------------------------------------------------------------------')

# 2 Comparez les températures 
# (january > 0).sum() > (january < 0).sum()
print("2) Il y avait plus de températures positives que négatives" if (january > 0).sum() > (january < 0).sum() \
      else  "2) Il y avait plus de températures négatives que positives")
print('--------------------------------------------------------------------------------------')

# 3 Pourcentage des températures > 0 sur le mois de Janvier
print(f'3) Pourcentage des températures supérieures à 0° sur le mois de Janvier : '
      f'{round((january > 0).sum() / len(january), 4) * 100}%')
print('--------------------------------------------------------------------------------------')

# 4  Créez un tableau days pour les jours du mois et donnez les jours pour lesquels 
# la température était supérieure à 0.
days_january = np.arange(1, january.size + 1, dtype=np.int8)
print(f'4) Jours du mois de Janvier où la température était supérieure à 0° : \n {days_january[january > 0]}')
print('--------------------------------------------------------------------------------------')

# 5 Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.
print(f'5) Tempéatures sur le mois de Janviers, supérieures à 0°, à partir du 10/01 : \n '
      f'{january[9:][january[9:] > 0]}')
print('--------------------------------------------------------------------------------------')

# 6 Les températures positives et on va calculer leur moyenne
avg = np.mean(january[january > 0])
january[january < 0] = avg

print(f'6) Moyenne des températures positives : {avg}')
print(f'6) Températures sur le mois de Janviers en remplaçant les températures négatives par la moyenne des '
      f'températures positives : \n {january}')
