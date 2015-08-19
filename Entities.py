from ebs import Entity
from Components import PolygonShape
from Components import Orientation
from Components import MoveSpeed
from Components import TurnSpeed
from Components import Health
from Components import FoodSeen
from Components import Collider
from NeuralNetwork import NeuralNetwork
from ShapeUtils import get_bounding_square

class Creature(Entity):
    BASE_SHAPE = [[10, 0], [0, -10], [-5, -5], [-5, 5], [0, 10]]
    MAX_HEALTH = 100

    def __init__(self, world, position, orientation, color):
        self.polygonshape = PolygonShape(self.BASE_SHAPE)
        self.position = position
        self.orientation = orientation
        self.color = color
        self.movespeed = MoveSpeed(0)
        self.turnspeed = TurnSpeed(0)

        self.neuralnetwork = NeuralNetwork(2, 7, 2)
        self.neuralnetwork.initialize_random_network()
        self.health = Health(self.MAX_HEALTH)
        self.foodseen = FoodSeen(0)

        bounding_square = get_bounding_square(self.BASE_SHAPE)
        self.collider = Collider(self, bounding_square, self.BASE_SHAPE)

class Food(Entity):
    def __init__(self, world, shape, position, color):
        self.polygonshape = PolygonShape(shape)
        self.position = position
        self.orientation = Orientation(0)
        self.color = color
