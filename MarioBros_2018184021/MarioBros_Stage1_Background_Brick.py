from pico2d import *

class Brick:  # 벽돌
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('Ground.png')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(68, 36, 17, 16, 300 - Move_locX, 107)
        self.image.clip_draw(68, 36, 17, 16, 332 - Move_locX, 107)
        self.image.clip_draw(68, 36, 17, 16, 364 - Move_locX, 107)

        self.image.clip_draw(68, 36, 17, 16, 1185 - Move_locX, 107)
        self.image.clip_draw(68, 36, 17, 16, 1217 - Move_locX, 107)

        for i in range(0, 10):
            self.image.clip_draw(68, 36, 17, 16, 1233 + i * 16 - Move_locX, 107 + 50)

        for i in range(0, 3):
            self.image.clip_draw(68, 36, 17, 16, 1453 + i * 16 - Move_locX, 107 + 50)

        self.image.clip_draw(68, 36, 17, 16, 1635 - Move_locX, 107)

        self.image.clip_draw(68, 36, 17, 16, 1980 - Move_locX, 107)

        for i in range(0, 3):
            self.image.clip_draw(68, 36, 17, 16, 2050 + i * 16 - Move_locX, 107 + 50)

        self.image.clip_draw(68, 36, 17, 16, 2150 - Move_locX, 107 + 50)
        self.image.clip_draw(68, 36, 17, 16, 2198 - Move_locX, 107 + 50)

        self.image.clip_draw(68, 36, 17, 16, 2169 - Move_locX, 107)
        self.image.clip_draw(68, 36, 17, 16, 2185 - Move_locX, 107)

        self.image.clip_draw(68, 36, 17, 16, 2900 - Move_locX, 107)
        self.image.clip_draw(68, 36, 17, 16, 2916 - Move_locX, 107)
        self.image.clip_draw(68, 36, 17, 16, 2948 - Move_locX, 107)