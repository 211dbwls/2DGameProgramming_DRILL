from pico2d import *

class Background:  # 배경
    image = None

    def __init__(self):
        if Background.image == None:
            Background.image = load_image('BlackBack.png')

    def draw(self):
        self.image.draw(400, 300)

class Ground:  # 땅
    image = None

    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('ScenerySprites2.gif')

        self.upx, self.downx = 8, 8

    def draw(self):
        from MarioBros_Mario import Move_locX

        self.upx = 8
        for i in range(0, 60):
            for j in range(0, 12):
                self.image.clip_draw(413, 1095, 16, 17, self.upx - Move_locX, 349 + 17 * j)
            self.upx += 16

        for j in range(0, 16):
            self.image.clip_draw(413, 1095, 16, 17, self.upx - Move_locX, 349 - 68 + 17 * j)

        for i in range(0, 28):
            for j in range(0, 7):
                self.image.clip_draw(413, 1095, 16, 17, self.upx - Move_locX, 349 + 17 * 5 + 17 * j)
            self.upx += 16

        for j in range(0, 16):
            self.image.clip_draw(413, 1095, 16, 17, self.upx - Move_locX, 349 - 68 + 17 * j)

        for i in range(0, 50):
            for j in range(0, 16):
                self.image.clip_draw(413, 1095, 16, 17, self.upx - Move_locX, 349 - 68 + 17 * j)
            self.upx += 16

        # 바닥
        self.downx = 8
        for t in range(0, 3):
            for i in range(0, 15 - t * 2):
                for j in range(0, 2):
                    self.image.clip_draw(413, 1095, 16, 17, self.downx + 16 * i - Move_locX, 124 + 34 * t + 17 * j)

        for i in range(0, 40):
            for j in range(0, 7):
                self.image.clip_draw(413, 1095, 16, 17, self.downx - Move_locX, 5 + 17 * j)
            self.downx += 16

        self.downx += 32
        for i in range(0, 25):
            for j in range(0, 7):
                self.image.clip_draw(413, 1095, 16, 17, self.downx - Move_locX, 5 + 17 * j)
            self.downx += 16

        self.downx += 32
        for i in range(0, 10):
            for j in range(0, 7):
                self.image.clip_draw(413, 1095, 16, 17, self.downx - Move_locX, 5 + 17 * j)
            self.downx += 16

        self.downx += 32
        for i in range(0, 75):
            for j in range(0, 7):
                self.image.clip_draw(413, 1095, 16, 17, self.downx - Move_locX, 5 + 17 * j)
            self.downx += 16

        self.downx += 362
        for i in range(0, 5):
            for j in range(0, 2):
                self.image.clip_draw(413, 1095, 16, 17, self.downx + 16 * i - Move_locX, 124 + 17 * j)

        for i in range(0, 5):
            for j in range(0, 7):
                self.image.clip_draw(413, 1095, 16, 17, self.downx - Move_locX, 5 + 17 * j)
            self.downx += 16

        for i in range(0, 23):
            for j in range(0, 7):
                self.image.clip_draw(413, 1095, 16, 17, self.downx - Move_locX, 5 + 17 * j)
            self.downx += 16

class FireGround:
    image = None

    def __init__(self):
        if FireGround.image == None:
            FireGround.image = load_image('ScenerySprites2.gif')

    def draw(self):
        from MarioBros_Mario import Move_locX

        self.image.clip_draw(620, 755, 35, 35, 656 - Move_locX, 10)
        self.image.clip_draw(620, 755, 35, 35, 656 - Move_locX, 30)
        self.image.clip_draw(620, 792, 35, 12, 656 - Move_locX, 54)

        self.image.clip_draw(620, 755, 35, 35, 1088 - Move_locX, 10)
        self.image.clip_draw(620, 755, 35, 35, 1088 - Move_locX, 30)
        self.image.clip_draw(620, 792, 35, 12, 1088 - Move_locX, 54)

        self.image.clip_draw(620, 755, 35, 35, 1280 - Move_locX, 10)
        self.image.clip_draw(620, 755, 35, 35, 1280 - Move_locX, 30)
        self.image.clip_draw(620, 792, 35, 12, 1280 - Move_locX, 54)

class BridgeGround:
    image = None

    def __init__(self):
        if BridgeGround.image == None:
            BridgeGround.image = load_image('ScenerySprites2.gif')

        self.x = 2507

    def draw(self):
        from MarioBros_Mario import Move_locX

        for i in range(0, 20):
            self.image.clip_draw(580, 770, 25, 15, self.x + 18 * i - Move_locX, 107)

        self.image.clip_draw(140, 1200, 40, 10, 2700 - Move_locX, 157)

class Brick:  # 벽돌
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('ScenerySprites2.gif')

    def draw(self):
        from MarioBros_Mario import Move_locX

        self.image.clip_draw(373, 1095, 16, 17, 968 - Move_locX, 264)

        self.image.clip_draw(373, 1095, 16, 17, 1180 - Move_locX, 264)

        self.image.clip_draw(373, 1095, 16, 17, 1416 - Move_locX, 264)
        self.image.clip_draw(373, 1095, 16, 17, 1630 - Move_locX, 264)
        self.image.clip_draw(373, 1095, 16, 17, 1844 - Move_locX, 264)
        self.image.clip_draw(373, 1095, 16, 17, 2058 - Move_locX, 264)
