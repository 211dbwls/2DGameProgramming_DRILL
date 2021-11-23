from pico2d import *

class Coin:  # 코인
    image = None

    def __init__(self):
        if Coin.image == None:
            Coin.image = load_image('ItemsSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 2 == 0:
            self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정
        self.time += 1

    def draw(self):
        pass