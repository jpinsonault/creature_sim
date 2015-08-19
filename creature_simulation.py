import pygame
from pygame.locals import *
from pprint import pprint
from ebs import World
from Systems import ShapeRenderer
from Systems import NeuralNetworkSystem
from Systems import MovingSystem
from Systems import CollisionSystem
from Entities import Creature
from Entities import Food
from Components import PolygonShape
from Components import Position
from Components import Orientation
from Components import Color
from QuadTree import QuadTree

WORLD_WIDTH = 100000
WORLD_HEIGHT = 100000


def main():
    screen = None
    sim_world = World()
    quadtree = QuadTree(
        bounds=(
            -WORLD_WIDTH/2,
            -WORLD_HEIGHT/2,
            WORLD_WIDTH,
            WORLD_HEIGHT),
        depth=9)

    sim_world.add_system(NeuralNetworkSystem())
    sim_world.add_system(MovingSystem())
    sim_world.add_system(CollisionSystem(quadtree))
    sim_world.add_system(ShapeRenderer(screen))


    Creature(sim_world, Position(4, 5), Orientation(50.0), Color(255, 255, 255))

    sim_world.process()

if __name__ == '__main__':
    main()
