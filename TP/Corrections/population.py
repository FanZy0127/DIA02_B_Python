import json
from random import randrange

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

levels = [4, 2, 3, 5, 7, 8, 2, 6, 4, 3, 5, 7, 5]


class Person:
    def __init__(self, person_object):
        self.id = person_object['id']
        self.name = person_object['name']
        self.relations = []
        self.relations_of_relations = []

    def add_relation(self, relation):
        if self.id != relation:
            self.relations.append(relation)

    def add_relation_of_relations(self, relations_array_array):
        for relations_array in relations_array_array:
            for relation in relations_array:
                if self.id != relation and relation not in self.relations_of_relations:
                    self.relations_of_relations.append(relation)

    def to_object(self):
        return {
            'id': self.id,
            'name': self.name,
            'relations': self.relations,
            'relations of relations': self.relations_of_relations
        }


class Relations:
    def __init__(self, population, relation_ships):
        self.population = population
        self.relation_ships = relation_ships

    def get_population_relations(self):
        for relation in self.relation_ships:
            for population in self.population:
                if population.id == relation[0]:
                    population.add_relation(relation[1])
                elif population.id == relation[1]:
                    population.add_relation(relation[0])
        self.set_population_relation_of_relations()
        return self.to_object()

    def set_population_relation_of_relations(self):
        for population in self.population:
            for relation in population.relations:
                relations_of_relations = [item.relations for item in self.population if item.id == relation]
                population.add_relation_of_relations(relations_of_relations)
        return self.to_object()

    def calc_moyenne_relations(self, round_param=2):
        result = 0
        for person in self.population:
            result += len(person.relations)

        return round(result / len(self.population), round_param)

    def users_relations(self):
        return {person.id: len(person.relations) for person in self.population}

    def users_relations_of_relations(self):
        return {person.id: person.relations_of_relations for person in self.population}

    def get_most_popular_people(self):
        result = self.population[0]
        for person in self.population:
            if len(person.relations) > len(result.relations):
                result = person
        return {result.name: len(result.relations)}

    def to_object(self):
        return [person.to_object() for person in self.population]


peoples = [Person(person_obj) for person_obj in populations]
relations = Relations(peoples, relationships)
print(relations.get_population_relations())
print(relations.calc_moyenne_relations())
print(relations.users_relations())
print(relations.get_most_popular_people())
print(relations.users_relations_of_relations())


# Exercice 2
print(sorted([student for student in zip(students, levels)], key=lambda x: x[1]))

# Exercice 3


class Dice:
    def __init__(self, name: str, values=None):
        if values is None:
            values = [1, 6]
        self.name = name
        self.values = values
        self.last_value = None


class Game:
    def __init__(self, dices: list):
        self.dices = dices

    def throw_dices(self, numbers_times: int):
        result = {}
        result2 = 0
        for _ in range(numbers_times):
            numbers_of_1 = 0
            for dice in self.dices:
                random_number = randrange(dice.values[0], dice.values[1] + 1)
                if dice.name not in result:
                    result[dice.name] = {}
                if random_number not in result[dice.name]:
                    result[dice.name][random_number] = 0
                result[dice.name][random_number] += 1
                dice.last_value = random_number

                if dice.last_value == 1:
                    numbers_of_1 += 1
                if numbers_of_1 == len(self.dices):
                    result2 += 1
        print(result2 / numbers_times)
        return result


dices = [Dice('Dé n°' + str(number)) for number in range(1, 4)]

print(Game(dices).throw_dices(1000))

# Exercice 4

data = relations.to_object()
with open("populations.json", "w") as file:
    json.dump(data, file)
