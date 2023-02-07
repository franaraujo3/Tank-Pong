from game import Game
from layouts import Layouts
from config import *

pygame.init()
pygame.joystick.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combat-Atari")
play = Game(screen, Layouts(1))
play.game_loop()
