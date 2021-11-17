from pico2d import *
import game_world

class UpMushroom:  # 1-UP 버섯 -> 목숨 + 1
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if UpMushroom.image == None:
            UpMushroom.image = load_image('ItemsSheet.png')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.movey = 0

    def update(self):
        if self.movey == 20:
            game_world.remove_object(self)
        else:
            self.movey += 5

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)


