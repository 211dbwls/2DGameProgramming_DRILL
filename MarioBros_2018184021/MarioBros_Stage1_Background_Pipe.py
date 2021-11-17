from pico2d import *

class LargePipe:
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if LargePipe.image == None:
            LargePipe.image = load_image('ScenerySprites.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 15, self.y - 40, self.x - Move_locX + 15, self.y + 38

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        draw_rectangle(*self.get_bb())
