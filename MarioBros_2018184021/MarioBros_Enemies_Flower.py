from pico2d import *

import game_framework

class Flower:  # 플라워
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Flower.image == None:
            Flower.image = load_image('EnemiesAnimationSheet.png')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.frame = 0  # 애니메이션 프레임
        self.time = 0  # update 시간 조절

        self.up = True
        self.movey = 0
        self.timer = 5.0

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 5, self.y + self.movey - 15, self.x - Move_locX + 15, self.y + self.movey + 8

    def update(self):
        self.timer -= game_framework.frame_time

        if self.up == True:
            if self.movey == 27:
                if self.timer <= 0:
                    self.up = False
                    self.timer = 5.0
            else:
                self.movey += 3
        else:
            if self.movey == 0:
                if self.timer <= 0:
                    self.up = True
                    self.timer = 5.0
            else:
                self.movey -= 3

        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션
        self.time += 1

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x - Move_locX, self.y + self.movey)

        # draw_rectangle(*self.get_bb())
