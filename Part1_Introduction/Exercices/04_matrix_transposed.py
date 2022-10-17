
matrix = [
    [1, 2, 3, 4, 5],  # i = 0
    [6, 7, 8, 9, 10],  # i = 1
    [11, 12, 13, 14, 15],  # i =2
]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

res = []
for i in range(len(matrix[0])):
    sub = []
    for row in matrix:
        sub.append(row[i])
    
    res.append(sub)

print(res)

# --- Compréhension de liste

n, p = len(matrix), len(matrix[0])
print(f'Length of the Matrix : {n}, Length of a sub matrix : {p}')
transposed = [[matrix[i][j] for i in range(n)] for j in range(p)]

print(transposed)

# Faire des fonctions

"""
dimension calcul la dimension de votre matrice en vérifiant également sa cohérence de manière défensive
"""
def dimension(m):
    n = len(m)
    assert n > 0
    p = len(m[0])
    assert p > 0
    for r in m:
        assert len(r) == p

    return n, p


"""
transpose qui permet de transposer une matrice 
"""
def transpose(m):
    n, p = dimension(m)

    return [[m[i][j] for i in range(n)] for j in range(p)]


print(transpose(matrix))


# Avec zip on peut également transposer une matrice mais on changera les lignes en tuple, donc ce n'est pas la solution,
# même si elle est intéressante à considérer.
"""
Chacune des lignes est assignée à une variable
"""
(x, y, z) = matrix

# On peut aussi récupérer la première ligne et les autres dans une liste
(x, *t) = matrix
# t -> [[6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# On peut zipper plusieurs listes 
list(zip([1, 2], [3, 4], [5, 6]))
# [(1, 3, 5), (2, 4, 6)]


print(list(zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15])))
print(list(zip(*matrix)))


"""
Pour bien comprendre un algorithme vous pouvez le faire tourner sur papier

res = []
for i in range(len(matrix[0])):
    sub = []
    for row in matrix:
        sub.append(row[i])
    
    res.append(sub)

print(res)

matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
]

Et vous faites tourner le premier algo de cette correction
res = []
i=0
     sub=[]
     sub= [1]
     sub= [1,6]
     sub= [1,6,11]
res = [[1,6,11]]

i = 1
     sub= []
     sub= [2]
     sub= [2,7]
     sub= [2,7,12]
res = [[1,6,11],[2,7,12] ]

i = 2
       sub= []
       sub= [3]
       sub= [3,8]
       sub= [3,8,13]
res = [[1,6,11],[2,7,12], [3,8,13] ]

i= 3

        sub= []
        sub= [4]
        sub= [4,9]
        sub= [4,9,14]
res = [[1,6,11],[2,7,12], [3,8,13], [4,9,14] ]

i= 4

       sub= []
       sub= [5]
       sub= [5,10]
       sub= [5,10,15]
res = [[1,6,11],[2,7,12], [3,8,13], [4,9,14], [5,10,15] ]
"""
