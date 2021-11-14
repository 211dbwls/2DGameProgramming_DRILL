from pico2d import *

class Star:  # 별
    image = None

    def __init__(self):
        if Star.image == None:
            Star.image = load_image('ItemsSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 4  # 제자리에서 색 변하도록 애니메이션 설정
        self.time += 1

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(0 + self.frame * 30, 0, 30, 30, 1654 - Move_locX, 130)