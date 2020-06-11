import pygame

# window dimensions
WIDTH = 600
HIGHT = 400

# Status Bar
bar_hight = 25

# colors
bg_color = (0, 132, 132)
red = (255, 0, 0)
black = (0, 0, 0)
grey = (200, 200, 200)

# Images
playerImg = pygame.image.load('img/player.png')
enemyImg = [pygame.image.load('img/enemy1.png'),
            pygame.image.load('img/enemy2.png')]

# directions
up = pygame.math.Vector2(0, -1)
down = pygame.math.Vector2(0, 1)
right = pygame.math.Vector2(1, 0)
left = pygame.math.Vector2(-1, 0)
down_right = down + right
down_left = down + left
up_right = up + right
up_left = up + left

# corner vectors
origin = pygame.math.Vector2(0, 0)
top_right = pygame.math.Vector2(WIDTH, 0)
bottom_right = pygame.math.Vector2(WIDTH, HIGHT)
bottom_left = pygame.math.Vector2(0, HIGHT)


# player initial data
player_dim = 10
player_offset = player_dim*up_left
player_vel = 5
player_pos = (WIDTH//2)*right + player_dim*down

# initial playfield data
padding = 30
init_vertices = [origin+padding*down_right,
                 top_right+padding*down_left,
                 bottom_right+padding*up_left, 
                 bottom_left+padding*up_right]
