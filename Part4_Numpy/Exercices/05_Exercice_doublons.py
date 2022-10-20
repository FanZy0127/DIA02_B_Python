import numpy as np

A = np.array([
    ["aaabbfffhjik", "hhhkkkiooo", "hhjuuk"],
    ["rrrtttyyuuii", "rroooiiiuuu", "jjjhhhaa"],
    ["aaabbgghhh", "iiikkkooomml", "hhhiijjjuu"],
    ["hhhyyytttuu", "xxxnnnooii", "kkkjjjuuppp"],
    ["qqqfffgghhh", "qqqkkklll", "ooohhhjjj"],
])

for i, line in enumerate(A):
    A[i] = [''.join(sorted(set(ch))) for ch in line]

print(A)

# Deuxième solution
sanitize = lambda a: [["".join(sorted(list(set(ch)))) for ch in line] for line in a]

print(f'SANITIZE DE A AVEC LAMBDA : {sanitize(A)}')
