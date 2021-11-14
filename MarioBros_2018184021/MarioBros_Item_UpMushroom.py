from pico2d import *

class UpMushroom:  # 1-UP 버섯 -> 목숨 + 1
    image = None

    def __init__(self):
        if UpMushroom.image == None:
            UpMushroom.image = load_image('ItemsSheet.png')

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(210, 60, 30, 30, 1820 - Move_locX, 127 + 50)
