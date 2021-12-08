from pico2d import *

import game_world
import game_framework

# boss_attack Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# boss_attack Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class Fire:
    image = None

    def __init__(self, x = 1200, y = 300, velocity = 1000):
        if Fire.image == None:
            Fire.image = load_image('EnemiesAnimationSheet.png')

        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 5, self.y - 7, self.x - Move_locX + 4, self.y + 4

    def update(self):
        from MarioBros_Mario import Move_locX


        self.x -= RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        # 화면을 벗어날 경우
        if (self.x - Move_locX) < 25 or (self.x - Move_locX) > 800 - 25:
            game_world.remove_object(self)

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(100 + int(self.frame) * 30, 0, 30, 10, self.x - Move_locX, self.y)

        # draw_rectangle(*self.get_bb())
