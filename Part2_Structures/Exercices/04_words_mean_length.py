import re

sentence = "Le langage Python est placé sous une licence libre proche de la licence BSD6 \
et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs \
centraux, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, \
iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs \
en offrant des outils de haut niveau et une syntaxe simple à utiliser."


sanitize = lambda p: re.sub(r"[^\w\s]", "", p, flags=re.IGNORECASE)
PRECISION = 2


def words_mean_length(sentence):
    sentence = sanitize(sentence).split()
    print(f'Sanitizing with sentence spliting : {sentence}')

    assert len(sentence) > 0

    return round(sum(len(word) for word in sentence) / len(sentence), PRECISION)


result = words_mean_length(sentence)
print(result)
