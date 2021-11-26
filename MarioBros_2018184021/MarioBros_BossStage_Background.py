from pico2d import *

class Background:  # 배경
    image = None

    def __init__(self):
        if Background.image == None:
            Background.image = load_image('BlackBack.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)

class Ground:  # 땅
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Ground.image == None:
            Ground.image = load_image('ScenerySprites2.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 10, self.y - 10, self.x - Move_locX + 7, self.y + 7

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        draw_rectangle(*self.get_bb())

class FireGround:
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if FireGround.image == None:
            FireGround.image = load_image('ScenerySprites2.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        # draw_rectangle(*self.get_bb())

class BridgeGround:
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if BridgeGround.image == None:
            BridgeGround.image = load_image('ScenerySprites2.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 10, self.y - 10, self.x - Move_locX + 7, self.y + 7

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        draw_rectangle(*self.get_bb())


class BridgeGroundUp:
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if BridgeGroundUp.image == None:
            BridgeGroundUp.image = load_image('ScenerySprites2.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x - Move_locX - 17, self.y - 5, self.x - Move_locX + 18, self.y + 5

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        draw_rectangle(*self.get_bb())

class Brick:  # 벽돌
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Brick.image == None:
            Brick.image = load_image('ScenerySprites2.gif')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

        # draw_rectangle(*self.get_bb())

