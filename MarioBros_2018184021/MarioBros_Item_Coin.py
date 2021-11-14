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
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(120, 0, 30, 30, 400, 575)  # 코인 개수 이미지

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 250 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 335 - Move_locX, 180)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 351 - Move_locX, 130)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1504 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1504 - Move_locX, 130 + 50)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1770 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1820 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1870 - Move_locX, 130)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 2169 - Move_locX, 130 + 50)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 2185 - Move_locX, 130 + 50)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 2935 - Move_locX, 130)