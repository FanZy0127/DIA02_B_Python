def mult(l, m):
    # une lambda est une fonction anonyme qui permet d'écrire un test court dans un algo
    check = lambda l: type(l) in [list, tuple] and len(l) > 0 and all(type(float(x)) == float for x in l)

    assert check(l) and check(m) and len(l) == len(m)

    s = 0
    for vec in zip(l, m):
        # unpacking pour assigner les valeurs à mes variables
        x, y = vec 
        s += float(x)*float(y)
    
    return s


print(mult([1, 2], [3, 4]))

