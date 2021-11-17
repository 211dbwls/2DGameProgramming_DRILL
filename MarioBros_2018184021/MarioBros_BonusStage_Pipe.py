from pico2d import *

class LPipe:
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if LPipe.image == None:
            LPipe.image = load_image('ScenerySprites.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def get_bb(self):
        return self.x - 18, self.y - 70, self.x + 40, self.y

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x, self.y)

        # draw_rectangle(*self.get_bb())

        self.image.clip_draw(70, 535, 80, 90, 760, 215)  # 위에 연결
        self.image.clip_draw(70, 535, 80, 90, 760, 305)
        self.image.clip_draw(70, 535, 80, 90, 760, 395)
        self.image.clip_draw(70, 535, 80, 90, 760, 485)
