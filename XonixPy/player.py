import pygame
from parameters import *


class Player(object):
    def __init__(self, color, posVec, dim, vel):
        self.color = color
        self.posVec = posVec
        self.dim = dim
        self.vel = vel
        self.velDir = pygame.math.Vector2()
        self.velVec = pygame.math.Vector2()

    def draw(self, surface):
        if not self.is_outside():
            self.posVec += self.velVec
        pygame.draw.rect(surface, self.color, (self.posVec.x, self.posVec.y, self.dim, self.dim))
        surface.blit(playerImg, self.posVec)

    def is_outside(self):
        if self.posVec.x < self.vel and self.velDir == left:
            return True
        if self.posVec.x > WIDTH -self.vel - self.dim and self.velDir == right:
            return True
        if self.posVec.y < self.vel and self.velDir == up:
            return True
        if self.posVec.y > HIGHT -self.vel - self.dim and self.velDir == down:
            return True

    def move(self, dir):
            self.velDir = dir
            self.velVec = self.vel * self.velDir

    def get_rect(self):
        return pygame.Rect(self.posVec.x, self.posVec.y, self.dim, self.dim)
