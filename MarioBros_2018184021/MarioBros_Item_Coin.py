from pico2d import *
import game_world

class Coin:  # 코인
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Coin.image == None:
            Coin.image = load_image('ItemsSheet.png')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.frame = 0
        self.up = True
        self.movey = 0

    def update(self):
        if self.up == True:
            self.movey += 10
            if self.movey == 50:
                self.up = False
        else:
            self.movey -= 10
            if self.movey == 0:
                game_world.remove_object(self)

        self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x - Move_locX, self.y + self.movey)

