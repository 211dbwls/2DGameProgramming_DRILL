from pico2d import *

class LargePipe:
    image = None

    def __init__(self):
        if LargePipe.image == None:
            LargePipe.image = load_image('ScenerySprites.gif')

    def draw(self):
        from MarioBros_Mario import Move_locX

        self.image.clip_draw(225, 490, 40, 80, 740 - Move_locX, 75)

        self.image.clip_draw(225, 490, 40, 80, 900 - Move_locX, 75)  # 보너스 맵 연결