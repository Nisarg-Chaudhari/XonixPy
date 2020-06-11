import pygame
from parameters import *

playfields = []


class Playfield(object):
    def __init__(self, vertices: list):
        self.vertices = vertices
        self.rect = None

    def draw(self, surface):
        self.rect = pygame.draw.polygon(surface, black, self.vertices)


