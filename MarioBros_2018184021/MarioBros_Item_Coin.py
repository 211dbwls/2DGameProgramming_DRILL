from pico2d import *

class Coin:  # 코인
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Coin.image == None:
            Coin.image = load_image('ItemsSheet.png')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.frame = 0
        self.time = 0  # update 시간 조절

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 9, self.y - 11, self.x - Move_locX + 2, self.y + 5

    def update(self):
        if self.time % 2 == 0:
            self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정
        self.time += 1

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(120, 0, 30, 30, 400, 575)  # 코인 개수 이미지

        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        draw_rectangle(*self.get_bb())
