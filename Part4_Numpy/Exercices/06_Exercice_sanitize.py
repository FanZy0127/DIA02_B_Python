import numpy as np

students = np.array([
    ["Name: Luce du Coulon", "phone: 201-20-30"],
    ["Name: Auguste Dupont", "phone: 201-22-30"],
    ["Name: Roger Le Voisi", "phone: 201-27-30"],
    ["Name: Alexandre Lacri", "phone: 201-10-30"],
    ["Name: Jacques Humber", "phone: 201-20-35"],
    ["Name: Thérèse Guille", "phone: 201-20-38"],
    ["Name: Gilles Gros-Bodin", "phone: 201-20-39"],
    ["Name: Amélie Pires", "phone: 201-25-39"],
    ["Name: Marcel Laporte", "phone: 201-20-39"],
    ["Name: Geneviève Marchal", "phone: 301-20-39"]
])

# 1
sanitize = lambda a, val_1, val_2: [[line[0][len(val_1):].strip(), line[1][len(val_2):].strip()] for line in a]

students_sanitize = np.array(sanitize(students, 'Name:', 'phone:'))
print(students_sanitize)


# 2
mask = ["30" in line[1].split("-") for line in students_sanitize]
print(mask)

print(len(students[mask]))
