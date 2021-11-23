from pico2d import *

class Brick:  # 벽돌
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Brick.image == None:
            Brick.image = load_image('ScenerySprites2.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def get_bb(self):
        return self.x - 7, self.y - 10, self.x + 7, self.y + 8

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x, self.y)

        draw_rectangle(*self.get_bb())
