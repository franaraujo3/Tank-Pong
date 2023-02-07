import wall
from config import *


class Layouts:
    layouts = []

    def __init__(self, layout_type: int):
        self.group = pygame.sprite.Group()
        self.get_screen()
        self.wall_color = "#d4a941"
        self.bg_color = "#861c09"
        self.rectangle()

        for layout in self.layouts[layout_type - 1]:
            self.group.add(wall.Wall(self.wall_color, layout[0], layout[1]))

    def get_group(self):
        return self.group

    def get_bg_color(self):
        return self.bg_color

    def rectangle(self):
        self.group.add(wall.Wall(self.wall_color, (screen_width, wall_width), (0, score_height)))
        self.group.add(wall.Wall(self.wall_color, (screen_width, wall_width), (0, screen_height-wall_width)))
        self.group.add(wall.Wall(self.wall_color, (wall_width, screen_height-100), (0, score_height+wall_width)))
        self.group.add(wall.Wall(self.wall_color, (wall_width, screen_height-100), (screen_width-wall_width, score_height + wall_width)))

    def get_screen(self):
        layout_temp = []
        with open('arena.txt') as f:
            lines = f.readlines()
        for line in range(len(lines)):
            for char in range(len(lines[line])):
                if lines[line][char] == '1':
                    layout_temp.append([RECT_1, (wall_width+char*RECT_1[0], wall_width+score_height+line*RECT_1[1])])

        self.layouts.append(layout_temp)
