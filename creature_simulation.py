import pygame
from pygame.locals import *
from pprint import pprint
from ebs import World
from Systems import ShapeRenderer
from Systems import Mover
from Entities import Creature
from Entities import Food
from Components import PolygonShape
from Components import Position
from Components import Orientation
from Components import Color


def main():
    sim_world = World()
    sim_world.add_system(ShapeRenderer(None))
    sim_world.add_system(Mover(None))

    Creature(sim_world,
             [[0, 1], [2, 3], [3, 4]],
             Position(5, 6),
             45.0,
             Color(255, 255, 255))
    Creature(sim_world,
             [[0, 1], [2, 3], [3, 4]],
             Position(5, 6),
             45.0,
             Color(255, 255, 255))
    Creature(sim_world,
             [[0, 1], [2, 3], [3, 4]],
             Position(5, 6),
             45.0,
             Color(255, 255, 255))
    Creature(sim_world,
             [[0, 1], [2, 3], [3, 4]],
             Position(5, 6),
             45.0,
             Color(255, 255, 255))

    Food(sim_world,
             [[0, 1], [2, 3], [3, 4]],
             Position(5, 6),
             Color(255, 255, 255))

    Food(sim_world,
             [[0, 1], [2, 3], [3, 4]],
             Position(5, 6),
             Color(255, 255, 255))


    sim_world.process()

if __name__ == '__main__':
    main()