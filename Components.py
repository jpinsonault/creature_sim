from collections import namedtuple

PolygonShape = namedtuple('PolygonShape', ["points"])

Position = namedtuple('Position', ["x", "y"])

Orientation = namedtuple('Orientation', ["angle"])

Color = namedtuple('Color', ["r", "g", "b"])

MoveSpeed = namedtuple('MoveSpeed', ["speed"])

TurnSpeed = namedtuple('TurnSpeed', ["speed"])