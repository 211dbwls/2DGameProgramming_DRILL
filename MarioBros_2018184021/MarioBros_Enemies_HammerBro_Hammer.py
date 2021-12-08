from pico2d import *

import game_world
import game_framework

# hammer Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# hammer Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class Hammer:
    image = None

    def __init__(self, x, y, velocity):
        if Hammer.image == None:
            Hammer.image = load_image('ScenerySprites2.gif')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(500, 100, 100, 100, self.x - Move_locX, self.y)

    def update(self):
        from MarioBros_Mario import Move_locX

        self.x += self.velocity

        # if (self.x - Move_locX) < 25 or (self.x - Move_locX) > 800 - 25:
        #     game_world.remove_object(self)


