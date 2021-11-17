from pico2d import *

class Brick:  # 벽돌
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('ScenerySprites2.gif')

    def update(self):
        pass

    def draw(self):
        for i in range(0, 3):
            for j in range(0, 30):
                self.image.clip_draw(393, 1134, 15, 16, 25 + 15 * i, 56 + 16 * j)

        for i in range(0, 22):
            for j in range(0, 5):
                self.image.clip_draw(393, 1134, 15, 16, 250 + 15 * i, 56 + 16 * j)

        for i in range(0, 22):
            for j in range(0, 3):
                self.image.clip_draw(393, 1134, 15, 16, 250 + 15 * i, 485 + 16 * j)