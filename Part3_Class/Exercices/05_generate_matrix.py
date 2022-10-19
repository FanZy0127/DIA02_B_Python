import random as r


class GenerateMatrix:

    r_min, r_max = 1, 20
    complexity = 100

    def __init__(self, n, p):
        self.dim = (n, p)
        self.Matrix = self.__run()

    def __run(self):
        n, p = self.dim

        return [
            [r.randint(GenerateMatrix.r_min, GenerateMatrix.r_max) for _ in range(p)] for _ in range(n)
        ]

    def shuffle(self):
        count = GenerateMatrix.complexity

        while count > 0:
            i, j = self.lines()
            # assignation par décomposition des valeurs de lignes
            self.Matrix[i], self.Matrix[j] = self.Matrix[j], self.Matrix[i]
            count -= 1

    def lines(self):
        n, p = self.dim

        i, j = r.randint(0, n-1), r.randint(0, n-1)
        while i == j:
            i, j = r.randint(0, n-1), r.randint(0, n-1)

        return i, j


GenerateMatrix.r_min = 0
GenerateMatrix.r_max = 10
GenerateMatrix.complexity = 1000

gen = GenerateMatrix(10, 8)

print(gen.Matrix)
gen.shuffle()
print(gen.Matrix)
