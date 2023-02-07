import pygame

pygame.font.init()
pygame.mixer.init()

# Screen
score_height = 50
wall_width = 25
screen_width = 800
screen_height = 550

# Text
score_font = pygame.font.Font('font/Gamer.ttf', 90)
victory_font = pygame.font.Font('font/Gamer.ttf', 100)

# Colors
RED = (134, 28, 9)
YELLOW = (212, 169, 65)
WHITE = (255, 255, 255)
GREEN = (0, 127, 33)
BLUE = (0, 97, 148)
DARKER_GREEN = (31, 61, 12)
DARKER_BLUE = (11, 11, 69)

# Rectangles constant
RECT_1 = (wall_width, wall_width)

# Screen refresh
fps = 60

# Clock
clk = pygame.time.Clock()

# Game
defeat_time = 50
max_score = 3
coords = [[400, 275], [40, 120], [40, 400],  [730, 120], [730, 400]]

# Tanks
TAM_TANK = 32
tank_sheets = [pygame.image.load("Sprites/Tank_"+str(x)+".png") for x in range(1, 6)]
rot_speed = 0.4
tank_speed = 3
ball_speed = 3
ball_bounce = 3

shot_time = 10

# Sounds
victory_sound_effect = pygame.mixer.Sound("Sounds/Yippeee.wav")
boom_sound_effect = pygame.mixer.Sound("Sounds/VineBoom.wav")
thud_sound_effect = pygame.mixer.Sound("Sounds/Thud.wav")
shot_sound_effect = pygame.mixer.Sound("Sounds/Shot.wav")
