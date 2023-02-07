from config import *


class Ball(pygame.sprite.Sprite):

    def __init__(self, tank, offset_x, offset_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.tank = tank
        self.x = tank.rect.x + offset_x
        self.y = tank.rect.y + offset_y
        self.cont = 0
        self.image = pygame.image.load('Sprites/testeball.png')
        self.image = pygame.transform.scale(self.image, (8 * 5, 8 * 5))
        self.group = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
        self.dx = vel_x
        self.dy = vel_y

    def update(self):
        # update balls in list
        self.move()
        if self.cont >= ball_bounce:
            self.cont = 0
            self.tank.ball_list.remove(self)
            self.tank.ball_sprites.remove(self)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
