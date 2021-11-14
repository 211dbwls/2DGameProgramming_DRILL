from pico2d import *

class LPipe:
    image = None

    def __init__(self):
        if LPipe.image == None:
            LPipe.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw(50, 500, 100, 130, 750, 110)

        self.image.clip_draw(70, 535, 80, 90, 760, 215)  # 위에 연결
        self.image.clip_draw(70, 535, 80, 90, 760, 305)
        self.image.clip_draw(70, 535, 80, 90, 760, 395)
        self.image.clip_draw(70, 535, 80, 90, 760, 485)
