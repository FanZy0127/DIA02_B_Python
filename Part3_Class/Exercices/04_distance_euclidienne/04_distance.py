import math as m
from distance import Point


class AverageDistance:
    precision = 2

    def __init__(self, *points: Point):
        self.points = points  # tuple de point
        self.euclidean_norm = lambda p, q: m.sqrt((p.x - q.x)**2 + (p.y - q.y)**2)
        self.absolute_norm = lambda p, q: abs(p.x - q.x) + abs(p.y - q.y)
        self.minkowski_norm = lambda p, q, r: (abs(p.x - q.x)**r + abs(p.y - q.y)**r)**(1/r)

    def euclidean(self, centroid: Point) -> float | int:
        assert len(self.points) > 0

        return round(
            sum(self.euclidean_norm(point, centroid) for point in self.points)/len(self.points),
            self.precision
         )

    def absolute(self, centroid: Point) -> float | int:
        assert len(self.points) > 0

        return round(
            sum(self.absolute_norm(point, centroid) for point in self.points)/len(self.points),
            self.precision
        )

    def minkowski(self, centroid: Point, root_value: float | int) -> float | int:
        assert len(self.points) > 0

        return round(
            sum(self.minkowski_norm(point, centroid, root_value) for point in self.points)/len(self.points),
            self.precision
        )


AverageDistance.precision = 4
centroid_point = Point(3, 7)
A = Point(5, 7)
B = Point(7, 1.3)
C = Point(10, 11)
D = Point(0.9, 11)
E = Point(3, 8)

avg_distance = AverageDistance(A, B, C, D, E)
order = 3

print(f'La distance absolue moyenne au point centroïde est de {avg_distance.absolute(centroid_point)}.')
print(f'La distance euclidienne moyenne au point centroïde est de {avg_distance.euclidean(centroid_point)}.')
print(f'La distance de Minkowski moyenne au point centroïde est de {avg_distance.minkowski(centroid_point, order)}.')
