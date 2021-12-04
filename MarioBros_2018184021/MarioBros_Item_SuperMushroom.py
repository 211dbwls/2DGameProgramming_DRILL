from pico2d import *
import game_world

class SuperMushroom:  # 슈퍼 버섯 -> 키 커짐
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if SuperMushroom.image == None:
            SuperMushroom.image = load_image('ItemsSheet.png')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.up = True
        self.movey = 0

    def update(self):
        if self.up == True:
            self.movey += 5
            if self.movey == 30:
                self.up = False
        else:
            self.movey -= 10
            if self.movey == 0:
                game_world.remove_object(self)

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y + self.movey)
