from pico2d import *
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

import game_framework

import server

# zombie Run Speed
# PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
# RUN_SPEED_KMPH = 10.0  # Km / Hour
# RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
# RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
# RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
# TIME_PER_ACTION = 0.5
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 3

class Boss:
    image = None

    def prepare_patrol_points(self):
        pass

    def __init__(self, left, bottom, width, height, x, y):
        if Boss.image == None:
            Boss.image = load_image('EnemiesAnimationSheet.png')

        # self.prepare_patrol_points()
        # self.patrol_order = 1

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.frame = 0

        self.dir = 1
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.wait_timer = 2.0

        # self.build_behavior_tree()

    def wander(self):  # 배회
        pass

    def wait(self):
        pass

    def find_player(self):
        pass

    def move_to_player(self):
        pass

    def get_next_position(self):
        pass

    def move_to_target(self):
        pass

    def build_behavior_tree(self):
        pass

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 20, self.y - 13, self.x - Move_locX + 20, self.y + 13

    def update(self):
        pass
        # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        # self.frame = (self.frame + 1) % 3

        # self.x += RUN_SPEED_KMPH * game_framework.frame_time
        # self.x = clamp(25, self.x, 3600)
        # self.x += self.speed * self.dir * game_framework.frame_time
        # self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        # self.x = clamp(50, self.x, 1280 - 50)
        # self.y = clamp(50, self.y, 1024 - 50)

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left + self.frame * 50, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        draw_rectangle(*self.get_bb())
