from pico2d import *

class FireFlower:  # 파이어 플라워 -> 불 공격
    image = None

    def __init__(self):
        if FireFlower.image == None:
            FireFlower.image = load_image('ItemsSheet.png')

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(140, 30, 30, 30, 1193 - Move_locX, 127)