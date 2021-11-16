from pico2d import *

import game_world

class FireBall:
    image = None

    def __init__(self, x = 1200, y = 65, velocity = 20):
        if FireBall.image == None:
            FireBall.image = load_image('ScenerySprites2.gif')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(660, 770, 20, 20, self.x - Move_locX, self.y)

    def update(self):
        from MarioBros_Mario import Move_locX

        self.x += self.velocity

        if (self.x - Move_locX) < 25 or (self.x - Move_locX) > 800 - 25:
            game_world.remove_object(self)


