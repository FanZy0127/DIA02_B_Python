import re


class HasCap:

    def __init__(self, sentence: str, sanitize=lambda p: re.sub(r"[^\w\s]", "", p, flags=re.IGNORECASE)):
        self.phrase = sanitize(sentence)

    def parse(self) -> dict:
        
        return {
            w: self.phrase.count(w) for w in self.phrase.split() if w[0].isupper()
        }


"""
Dataset
"""

sentence_to_hashcap = "Le langage Python est placé sous une licence libre proche de la licence BSD6 et fonctionne " \
                      "sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux, " \
                      "de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, " \
                      "et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des " \
                      "programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser. " \
                      "Python Python."

hascap = HasCap(sentence_to_hashcap)

print(hascap.parse())
