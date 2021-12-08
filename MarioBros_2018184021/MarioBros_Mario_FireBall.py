from pico2d import *

import game_world

class FireBall:
    image = None

    def __init__(self, x = 1200, y = 65, velocity = 200):
        if FireBall.image == None:
            FireBall.image = load_image('ScenerySprites2.gif')

        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 5, self.y - 7, self.x - Move_locX + 4, self.y + 4

    def update(self):
        from MarioBros_Mario import Move_locX

        self.x += self.velocity
        self.frame = (self.frame + 1) % 4

        # 화면 벗어날 경우
        if (self.x - Move_locX) < 25 or (self.x - Move_locX) > 800 - 25:
            game_world.remove_object(self)

        # 굼바와 충돌

        # 해머브러스와 충돌

    def draw(self):
       from MarioBros_Mario import Move_locX
       self.image.clip_draw(313 + self.frame * 12, 300, 8, 10, self.x - Move_locX, self.y)

       draw_rectangle(*self.get_bb())

