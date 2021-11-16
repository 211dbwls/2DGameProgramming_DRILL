import random
from pico2d import *
import game_world
import game_framework

BIRD_PIXEL_PER_METER = (100.0 / 3.0)  # 이미지가 100 pixel이므로 300cm로 설정함(100 pixel 300 cm)
BIRD_SPEED_KMPH = 29.0  # 참새의 속도가 29 ~ 40km이므로 여기서는 29km로 설정함
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * BIRD_PIXEL_PER_METER)

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14  # 프레임은 14개로 나눠져있으므로 14로 설정

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')

        self.x, self.y, self.velocity = random.randint(50, 1600 - 50), random.randint(350, 550), BIRD_SPEED_PPS
        self.dir = random.randint(0, 1)
        self.frame = random.randint(0, 14)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.dir == 1:
            if self.x > 1550:
                self.dir = 0
            else:
                self.x += self.velocity
        elif self.dir == 0:
            if self.x < 50:
                self.dir = 1
            else:
                self.x -= self.velocity
