import pygame
from parameters import *
from statusBar import *
from player import *
from playfield import *


pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((WIDTH, HIGHT+bar_hight))
pygame.display.set_caption("XonixPy")

newPlayer = Player(bg_color, player_pos, player_dim, player_vel)
init_playfield = Playfield(init_vertices)
playfields.append(init_playfield)


# initial display setup
win.fill(bg_color)
init_playfield.draw(win)
newPlayer.draw(win)
pygame.display.update()


def game_logic():
    for playfield in playfields:
        if newPlayer.get_rect().colliderect(playfield.rect):
            newPlayer.color = red
        else:
            newPlayer.color = bg_color


def display_refresh():

    win.fill(bg_color)
    draw_status_bar(win)
    init_playfield.draw(win)
    newPlayer.draw(win)
    pygame.display.update()


run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            newPlayer.posVec = pygame.math.Vector2(pygame.mouse.get_pos())
            newPlayer.velVec *= 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        newPlayer.move(up)
    if keys[pygame.K_DOWN]:
        newPlayer.move(down)
    if keys[pygame.K_LEFT]:
        newPlayer.move(left)
    if keys[pygame.K_RIGHT]:
        newPlayer.move(right)
    if keys[pygame.K_SPACE]:
        newPlayer.posVec = pygame.math.Vector2(player_pos)
        newPlayer.velVec *= 0

    game_logic()
    display_refresh()

pygame.quit()
