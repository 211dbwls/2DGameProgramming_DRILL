from pico2d import *

class Fire:
    image = None

    def __init__(self, x = 1200, y = 300, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image('EnemiesAnimationSheet.png')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        from MarioBros_Mario import Move_locX
        # self.image.clip_draw(100, 0, 30, 10, self.x - Move_locX, self.y)

    def update(self):
        pass
        # self.x += self.velocity
