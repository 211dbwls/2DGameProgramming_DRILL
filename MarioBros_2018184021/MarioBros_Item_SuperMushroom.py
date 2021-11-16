from pico2d import *

class SuperMushroom:  # 슈퍼 버섯 -> 키 커짐
    image = None

    def __init__(self):
        if SuperMushroom.image == None:
            SuperMushroom.image = load_image('ItemsSheet.png')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(180, 60, 30, 30, 319 - Move_locX, 127)