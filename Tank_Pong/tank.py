import math
from ball import Ball
from config import *


class Tank(pygame.sprite.Sprite):
    def __init__(self, sheet, pos, current_sprite, joystick):
        super().__init__()
        self.score = 0
        self.joystick = joystick
        self.img_tank = []
        self.ball_list = []
        self.ball_sprites = pygame.sprite.Group()
        for i in range(4):
            for j in range(4):
                self.img_tank.append(sheet.subsurface((j*48, i*48), (48, 48)))
        self.direction = current_sprite
        self.image = self.img_tank[self.direction]
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.x = pos[0]
        self.y = pos[1]
        self.rot = 0
        self.moveW = False
        self.shoot = False
        self.hit = False
        self.stop = False
        self.shoot_time = 0

    def shoot_(self):
        self.shoot = True

    def no_move_w(self):
        self.moveW = False

    def move_w(self):
        self.moveW = True

    def no_rot(self):
        self.rot = 0

    def rotate(self, rotation):
        self.rot = rotation

    def reposition(self, choice):
        self.stop = False
        self.hit = False
        self.x = choice[0]
        self.y = choice[1]

    def update(self):
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        if self.stop:
            return
        self.shoot_time -= 1
        self.direction -= self.rot
        if self.direction < 0:
            self.direction = 15
        if self.direction > 15:
            self.direction = 0
        self.image = self.img_tank[int(self.direction)]
        if self.hit:
            self.direction -= 0.8
            return
        vel_x = math.cos((2-int(self.direction)/8)*math.pi)
        vel_y = -math.sin((2-int(self.direction)/8)*math.pi)
        if self.moveW:
            self.x += vel_x * 2
            self.y += vel_y * 2
        if self.shoot and self.shoot_time <= 0 and len(self.ball_list) <= 2:
            self.shoot_time = shot_time
            ball = Ball(self, 3+vel_x*15, 5+vel_y*18, vel_x*4, vel_y*4)
            self.ball_sprites.add(ball)
            self.ball_list.append(ball)
            shot_sound_effect.play()
        if self.shoot:
            self.shoot = False
