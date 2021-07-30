
<h2 align='center'> Assignment - Iterable:-  Polygon Sequence </h2>

## Objective:
- Convert the Polygon class such that all it's properties are evaluated lazily.
- Convert the PolygonSequence class to an **iterable**, and make sure all the properties of the Sequence class are also evaluated lazily. 

### Polygon Class

The `Polygon` class is rewritten using the `property` and `setter` decorator such that the properties are lazily evaluated. Another advantage of using `property` and `setter` decorators to access and set properties is that sanitary checks can be performed on the class properties at the time of assignment.  The `init_parameters` method is used to initialize all the property values.

<h3 align='left'> Polygon Sequence Class</h3>

The `PolygonSequence` class can be converted to an `iterable` by adding an `iter` method, which calls the `PolygonIter` class. The `PolygonIter` class is an `iterator` (the `__iter__` method returns `self`), which implements the `__next__` and `__iter__` methods.

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




A Deepnote notebook demonostrating that the changes to the PolygonSequence class can be found [here](https://deepnote.com/project/EPAi3-session-12-medonmol-v90wkXt3Q_m-kk_etTlsKw/%2Fnotebook.ipynb)