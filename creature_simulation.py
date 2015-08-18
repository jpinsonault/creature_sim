import pygame
from pygame.locals import *
from pprint import pprint
from ebs import World
from Systems import ShapeRenderer
from Systems import NeuralNetworkSystem
from Systems import MovingSystem
from Entities import Creature
from Entities import Food
from Components import PolygonShape
from Components import Position
from Components import Orientation
from Components import Color


def main():
    screen = None
    sim_world = World()
    sim_world.add_system(NeuralNetworkSystem())
    sim_world.add_system(MovingSystem())
    sim_world.add_system(ShapeRenderer(screen))


    Creature(sim_world, Position(4, 5), Orientation(50.0), Color(255, 255, 255))

    sim_world.process()

if __name__ == '__main__':
    main()