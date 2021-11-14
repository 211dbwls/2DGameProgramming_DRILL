from pico2d import *

class Castle:
    image = None

    def __init__(self):
        if Castle.image == None:
            Castle.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(250, 0, 100, 100, 3500 - Move_locX, 90)