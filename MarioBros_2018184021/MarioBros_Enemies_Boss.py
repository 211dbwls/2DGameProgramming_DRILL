from pico2d import *

class Boss:  # 코인
    image = None

    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image('EnemiesAnimationSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        pass
        #if self.time % 2 == 0:
        #    self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정
        #self.time += 1

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(0, 10, 40, 50, 2820 - Move_locX, 130)
