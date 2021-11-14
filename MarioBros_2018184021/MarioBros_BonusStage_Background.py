from pico2d import *

class Background:  # 배경
    image = None

    def __init__(self):
        if Background.image == None:
            Background.image = load_image('BlackBack.png')

    def draw(self):
        self.image.draw(400, 300)

class Ground:  # 땅
    image = None

    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('ScenerySprites2.gif')

    def draw(self):
        for i in range(0, 48):
            for j in range(0, 3):
                self.image.clip_draw(392, 1112, 16, 17, 24 + 16 * i, 5 + 17 * j)
