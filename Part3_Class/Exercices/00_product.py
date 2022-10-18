"""
Ci dessous on a un exemple de getter/setter définit avec des décorateurs

"""


class Product:

    def __init__(self, name: str, price: float | int, tva: float | int = .2):
        self._price = price
        self._tva = tva
        self._name = name

    @property
    def price(self) -> float | int:
        return (self.tva + 1) * self._price

    @price.setter
    def price(self, price: float | int):
        self._price = price

    @property
    def tva(self) -> float | int:
        return self._tva

    @tva.setter
    def tva(self, tva: float | int):
        self._tva = tva

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def set_price(self, price: float | int):
        self._price = price

    def set_name(self, name: str):
        self._name = name


apple = Product("pomme",  1.2)
orange = Product("orange", 1.1)
print(f'Une {apple.name} coûte {apple.price}€.')
print(f'Une {orange.name} coûte {orange.price}€.')

products_sum = apple.price + orange.price
print(f'Le coût total pour une {apple.name} et une {orange.name} est de {products_sum}€.')
apple.set_price(2.05)
apple.set_name('Pink Lady')
print(f'Le nouveau prix de la {apple.name} est de {apple.price}€.')
