import random as r


def max_list(l: list) -> tuple:
    assert type(l) == list and len(l) > 0
    m = l[0]

    for el in l:
        if el > m:
            m = el

    return m, l.index(m)


final_list = []

# Crée un exemple
# r.randint retourne un entier aléatoire compris entre 1 et 100
# _ dans le range pour ne pas 
final_list.extend(r.randint(1, 101) for _ in range(20))

print(final_list)
print(max_list(final_list))
