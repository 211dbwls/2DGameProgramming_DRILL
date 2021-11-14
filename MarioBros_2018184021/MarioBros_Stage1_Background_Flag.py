from pico2d import *

class Flag:
    image = None

    def __init__(self):
        if Flag.image == None:
            Flag.image = load_image('ScenerySprites.gif')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        pass
        #if self.time % 3 == 0:
        #    self.frame = (self.frame + 1) % 5  # 깃발 내려가도록
        #self.time += 1

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(247 - self.frame * 33, 185, 25, 170, 3370 - Move_locX, 130)