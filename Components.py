from namedlist import namedlist

PolygonShape = namedlist('PolygonShape', ["points"])

Position = namedlist('Position', ["x", "y"])

Orientation = namedlist('Orientation', ["angle"])

Color = namedlist('Color', ["r", "g", "b"])

MoveSpeed = namedlist('MoveSpeed', ["speed"])

TurnSpeed = namedlist('TurnSpeed', ["speed"])

Health = namedlist('Health', ["amount"])

FoodSeen = namedlist('FoodSeen', ["number"])

# Collider = namedlist('Collider', ["entity", "bounding_square", "shape"])

class Collider(object):
    def __init__(self, entity, bounding_square, shape):
        self.entity = entity
        self.bounding_square = bounding_square
        self.shape = shape

    def __repr__(self):
        repr_string = "{}(entity={}, bounding_square={}, shape={})"
        name = self.__class__.__name__
        return repr_string.format(name, self.entity, self.bounding_square, self.shape)
