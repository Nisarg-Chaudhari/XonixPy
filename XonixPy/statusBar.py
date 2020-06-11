import pygame
from parameters import *

def draw_status_bar(surface):
    pygame.draw.rect(surface, grey, (0, HIGHT, WIDTH, bar_hight))