from pico2d import *

class Background:  # 배경
    image = None

    def __init__(self):
        if Background.image == None:
            Background.image = load_image('BlackBack.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)

class Ground:  # 땅
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Ground.image == None:
            Ground.image = load_image('ScenerySprites2.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x, self.y)

        draw_rectangle(*self.get_bb())

