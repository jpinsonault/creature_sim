from ebs import Applicator
from ebs import System
from Components import PolygonShape
from Components import Position
from Components import Orientation
from Components import Color
from Components import MoveSpeed
from Components import TurnSpeed

class ShapeRenderer(Applicator):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.componenttypes = (PolygonShape, Position, Orientation, Color)

    def process(self, world, componentsets):
        for polygonshape, position, orientation, color in componentsets:
            print("Rendering shape at {}".format(position))


class Mover(Applicator):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.componenttypes = (Position, Orientation, MoveSpeed, TurnSpeed)

    def process(self, world, componentsets):
        for polygonshape, position, movespeed, turnspeed in componentsets:
            print("Moving entity at {}, going at {}, turning at {}".format(position, movespeed, turnspeed))

