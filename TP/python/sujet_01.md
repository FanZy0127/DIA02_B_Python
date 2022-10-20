# TP 01 

```python
populations = [
    {"id": 0, "name": "Alan"},
    {"id": 1, "name": "Albert"},
    {"id": 2, "name": "Jhon"},
    {"id": 3, "name": "Brice"},
    {"id": 4, "name": "Alexendra"},
    {"id": 5, "name": "Brad"},
    {"id": 6, "name": "Carl"},
    {"id": 7, "name": "Dallas"},
    {"id": 8, "name": "Dennis"},
    {"id": 9, "name": "Edgar"},
    {"id": 10, "name": "Erika"},
    {"id": 11, "name": "Isaac"},
    {"id": 12, "name": "Ian"}
]

relationships = [
    [0, 1], [0, 2], [1, 2], [1, 4], [2, 3], [2, 5],
    [3, 4], [3, 7], [4, 5], [4, 8], [4, 9], [5, 7],
    [5, 9], [6, 7], [6, 8], [7, 1], [7, 8], [8, 9],
    [10, 1], [10, 2], [10, 3], [11, 12], [11, 2], [11, 5]
]

```

1. Modifiez la liste populations pour ajouter les relations (liste relationships) de chaque user de cette population, vous pouvez par exemple ajoutez une clé "relation", choisissez bien le type de cette relation, par exemple une liste vide. Puis placez les relations de chaque user dans la liste populations en utilisant relationships.

2. Calculer la moyenne des relations.

3. Créez une liste représentant les users (id) et le nombre de relation(s) qu'ils possèdent. 

4. Et retournez l'utilisateur qui possède le plus de relation(s).

5. Trouvez les amis des amis de chaque utilisateur. 

### Partie 2

Chaque étudiant a un niveau, ordonnez les étudiants par niveau dans un tableau students modidifé.

```python
students = [
    "Alan",
    "Albert",
    "Jhon",
    "Brice",
    "Alexendra",
    "Brad",
    "Carl",
    "Dallas",
    "Dennis",
    "Edgar",
     "Erika",
     "Isaac",
    "Ian" 
]

levels = [4,2,3,5,7,8,2,6,4,3,5, 7, 5]
``` 

### Partie 3

Créez un jeu de 3 dés et claculez la chance d'obtenir trois fois de suite un 1. Simulez l'expérience de jeu et comparez le résultat avec le résultat théorique.


Vérifiez que la théorie et la simulation sont proches.


### Partie 4

En utilisant la documentation doc Python.

1. Créez un fichier populations.json. Ajoutez-y les relations que vous avez créées.

2. Ajoutez l'user suivant dans ce même fichier.

rmq : respectez l'ouverture et la fermeture des fichiers.