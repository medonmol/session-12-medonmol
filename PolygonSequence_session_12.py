from Polygon_session_12 import Polygon


class PolygonSequence:
    def __init__(self, max_edge, radius):
        self.max_edge = max_edge
        self.radius = radius
        self.init_parameters()

    def init_parameters(self):
        _ = self.max_edge
        _ = self.radius
        _ = self.max_efficiency

    @property
    def max_edge(self):
        return self._max_edge

    @max_edge.setter
    def max_edge(self, new_max_edge):
        if not isinstance(new_max_edge, (int, float)):
            raise ValueError
        if new_max_edge < 3:
            raise ValueError
        self._max_efficiency = None
        self._max_edge = new_max_edge

    @property
    def radius(self):

        return self._radius

    @radius.setter
    def radius(self, rad):
        if not isinstance(rad, (int, float)):
            raise ValueError
        if rad < 0:
            raise ValueError

        self._max_efficiency = None
        self._radius = rad

    def __repr__(self):
        return f"Polygon Sequence class with max_edge = {self.max_edge} and common radius = {self.radius}"

    @property
    def max_efficiency(self):
        if self._max_efficiency is None:
            _polygons = sorted(
                self, key=lambda poly: poly.area / poly.perimeter, reverse=True
            )
            self._max_efficiency = _polygons[0]
        return self._max_efficiency

    def __iter__(self):
        return self.PolygonIter(self)

    class PolygonIter:
        def __init__(self, polygon_object):
            self._polygon_object = polygon_object
            self._idx = 3

        def __iter__(self):
            return self

        def __next__(self):
            if self._idx > self._polygon_object.max_edge:
                raise StopIteration
            else:
                poly = Polygon(self._idx, self._polygon_object.radius)
                self._idx += 1
                return poly
