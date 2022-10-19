import math as m


class Point:
    def __init__(self, x: float | int, y: float | int):
        self._x = x
        self._y = y

    @property
    def x(self) -> float | int:
        return self._x
    
    @x.setter
    def x(self, x: float | int):
        self._x = float(x)

    @property
    def y(self) -> float | int:
        return self._y
    
    @y.setter
    def y(self, y: float | int):
        self._y = float(y)


class Distance:

    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def euclidean(self):

        return m.sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2)
    

if __name__ == "__main__":
    A = Point(5, 7)
    B = Point(15, 1)
    distance = Distance(A, B)

    print(f"La distance euclidienne entre les deux points est de {distance.euclidean()}")
