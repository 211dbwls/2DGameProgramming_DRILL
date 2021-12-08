from pico2d import *

import server
import collision

class Flag:
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Flag.image == None:
            Flag.image = load_image('ScenerySprites.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.frame = 0
        self.time = 0  # update 시간 조절

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 5, self.y - 85, self.x - Move_locX + 12, self.y + 80

    def update(self):
        if collision.collide(self, server.mario):  # 마리오와 충돌했을 경우
            if self.frame < 4:
                self.frame = self.frame + 1  # 깃발 내려가도록


    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left - (self.frame * 33), self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        # draw_rectangle(*self.get_bb())
