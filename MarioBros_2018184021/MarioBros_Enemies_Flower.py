from pico2d import *

class Flower:  # 플라워
    image = None

    def __init__(self):
        if Flower.image == None:
            Flower.image = load_image('EnemiesAnimationSheet.png')

        self.frame = 0  # 애니메이션 프레임
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션
        self.time += 1

    def draw(self):
        pass
        # self.image.clip_draw(380 + self.frame * 30, 205, 30, 30, 600 - Move_locX, 60)
