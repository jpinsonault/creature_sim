from ebs import Applicator
from ebs import System
from Components import PolygonShape
from Components import Position
from Components import Orientation
from Components import Color
from Components import MoveSpeed
from Components import TurnSpeed
from Components import Health
from Components import FoodSeen
from NeuralNetwork import NeuralNetwork

class ShapeRenderer(Applicator):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.componenttypes = (PolygonShape,
                               Position,
                               Orientation,
                               Color)

    def process(self, world, componentsets):
        for polygonshape, position, orientation, color in componentsets:
            print("Rendering shape at {}".format(position))


class MovingSystem(Applicator):
    def __init__(self):
        super().__init__()
        self.componenttypes = (Position,
                               Orientation,
                               MoveSpeed,
                               TurnSpeed)

    def process(self, world, componentsets):
        for position, orientation, movespeed, turnspeed in componentsets:
            print("Moving entity at {}, going at {}, turning at {}".format(position, movespeed, turnspeed))


class NeuralNetworkSystem(Applicator):
    def __init__(self):
        super().__init__()
        self.componenttypes = (NeuralNetwork,
                               MoveSpeed,
                               TurnSpeed,
                               Health,
                               FoodSeen)

    def process(self, world, componentsets):
        for neuralnetwork, movespeed, turnspeed, health, foodseen in componentsets:
            neuralnetwork.set_inputs([health.amount, foodseen.number])
            neuralnetwork.compute_network()
            outputs = neuralnetwork.get_outputs()

            turnspeed.speed = outputs[0] / 200.0
            movespeed.speed = outputs[1] / 6.0

            print("Updated NN, outputs: {}, {} ".format(turnspeed, movespeed))
