seq = [1, 2, 3]
l = [1, 3, 7, 8, 9, 1, 2, 3, 8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]

string = 'Un chasseur sachant chasser doit savoir chasser sans son chien'
hunter = 'chasseur'
hunt = 'chasser'


def search_sequence(haystack, needle):
    res = list()
    for index in range(1 + len(haystack) - len(needle)):
        counter = 0
        # Tant que les caractères match avec les caractères de la liste, on avance.
        while counter < len(needle) and needle[counter] == haystack[index + counter]:
            counter += 1

        # Si la longueur du matching est égale à la longueur de la séquence recherchée...
        # alors, on a trouvé une séquence
        if counter == len(needle):
            res.append(index)

    return res


result = search_sequence(l, seq)

print(result)
print(search_sequence(string, hunter))
print(search_sequence(string, hunt))

# en compréhension de liste et slicing on obtient quelque chose de très concis
result_2 = [i for i in range(1 + len(l) - len(seq)) if l[i:(i+len(seq))] == seq]
result_3 = [i for i, indice in enumerate(l) if l[i:i + len(seq):] == seq]


print(result_2)
