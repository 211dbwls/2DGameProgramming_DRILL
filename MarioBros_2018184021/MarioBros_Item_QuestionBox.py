from pico2d import *

class QuestionBox:  # 물음표 상자
    image = None

    def __init__(self):
        if QuestionBox.image == None:
            QuestionBox.image = load_image('ItemsSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 3  # 제자리에서 색 변하도록 애니메이션 설정
        self.time += 1

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 250 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 319 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 335 - Move_locX, 100 + 50)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 351 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 980 - Move_locX, 100 + 30)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1204 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1504 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1504 - Move_locX, 100 + 50)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1654 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1770 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1820 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1820 - Move_locX, 100 + 50)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1870 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 2169 - Move_locX, 100 + 50)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 2185 - Move_locX, 100 + 50)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 2935 - Move_locX, 100)