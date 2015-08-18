from ebs import Entity
from Components import PolygonShape
from Components import Orientation
from Components import MoveSpeed
from Components import TurnSpeed

class Creature(Entity):
    def __init__(self, world, shape, position, orientation, color):
        self.polygonshape = PolygonShape(shape)
        self.position = position
        self.orientation = Orientation(orientation)
        self.color = color
        self.movespeed = MoveSpeed(0)
        self.turnspeed = TurnSpeed(0)

class Food(Entity):
    def __init__(self, world, shape, position, color):
        self.polygonshape = PolygonShape(shape)
        self.position = position
        self.orientation = Orientation(0)
        self.color = color
