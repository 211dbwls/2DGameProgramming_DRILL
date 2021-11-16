from pico2d import *

class Background:  # 배경
    image = None

    def __init__(self):
        if Background.image == None:
            Background.image = load_image('Back.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)

class StartSign:  # 시작 표지판
    image = None

    def __init__(self):
        if StartSign.image == None:
            StartSign.image = load_image('GroundSheet.png')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(195, 90, 38, 55, 100 - Move_locX, 56)

class BigCloud:  # 구름
    image = None

    def __init__(self):
        if BigCloud.image == None:
            BigCloud.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(140, 850, 70, 40, 550 - Move_locX, 300)
        self.image.clip_draw(140, 850, 70, 40, 900 - Move_locX, 300 + 50)

        self.image.clip_draw(140, 850, 70, 40, 1200 - Move_locX, 300)

        self.image.clip_draw(140, 850, 70, 40, 2100 - Move_locX, 300)

        self.image.clip_draw(140, 850, 70, 40, 3000 - Move_locX, 300)

        self.image.clip_draw(140, 850, 70, 40, 3150 - Move_locX, 300 + 50)

class SmallCloud:  # 구름
    image = None

    def __init__(self):
        if SmallCloud.image == None:
            SmallCloud.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(210, 855, 35, 30, 200 - Move_locX, 300)
        self.image.clip_draw(210, 855, 35, 30, 300 - Move_locX, 300 + 50)
        self.image.clip_draw(210, 855, 35, 30, 650 - Move_locX, 300 + 50)

        self.image.clip_draw(210, 855, 35, 30, 1000 - Move_locX, 300)
        self.image.clip_draw(210, 855, 35, 30, 1100 - Move_locX, 300)

        self.image.clip_draw(210, 855, 35, 30, 1350 - Move_locX, 300 + 50)

        self.image.clip_draw(210, 855, 35, 30, 1750 - Move_locX, 300)

        self.image.clip_draw(210, 855, 35, 30, 1900 - Move_locX, 300 + 50)

        self.image.clip_draw(210, 855, 35, 30, 2700 - Move_locX, 300)

        self.image.clip_draw(210, 855, 35, 30, 2850 - Move_locX, 300 + 50)

        self.image.clip_draw(210, 855, 35, 30, 3420 - Move_locX, 300)

class BigMountain:  # 산
    image = None

    def __init__(self):
        if BigMountain.image == None:
            BigMountain.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(80, 900, 90, 60, 180 - Move_locX, 60)

        self.image.clip_draw(80, 900, 90, 60, 800 - Move_locX, 60)

        self.image.clip_draw(80, 900, 90, 60, 1600 - Move_locX, 60)

        self.image.clip_draw(80, 900, 90, 60, 3300 - Move_locX, 60)

class SmallMountain:  # 산
    image = None

    def __init__(self):
        if SmallMountain.image == None:
            SmallMountain.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(170, 900, 50, 60, 400 - Move_locX, 60)

        self.image.clip_draw(170, 900, 50, 60, 1000 - Move_locX, 60)

        self.image.clip_draw(170, 900, 50, 60, 1875 - Move_locX, 60)

        self.image.clip_draw(170, 900, 50, 60, 3560 - Move_locX, 60)

class BigGrass:  # 풀
    image = None

    def __init__(self):
        if BigGrass.image == None:
            BigGrass.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(220, 900, 70, 60, 350 - Move_locX, 65)

        self.image.clip_draw(220, 900, 70, 60, 670 - Move_locX, 65)

        self.image.clip_draw(220, 900, 70, 60, 950 - Move_locX, 65)

        self.image.clip_draw(220, 900, 70, 60, 1440 - Move_locX, 65)

        self.image.clip_draw(220, 900, 70, 60, 1820 - Move_locX, 65)

class SmallGrass:  # 풀
    image = None

    def __init__(self):
        if SmallGrass.image == None:
            SmallGrass.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(290, 900, 30, 60, 1120 - Move_locX, 65)

        self.image.clip_draw(290, 900, 30, 60, 2010 - Move_locX, 65)

        self.image.clip_draw(290, 900, 30, 60, 2900 - Move_locX, 65)

        self.image.clip_draw(290, 900, 30, 60, 3520 - Move_locX, 65)

class Ground:  # 땅
    image = None

    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('Ground.png')

        self.left, self.bottom = 2, 155  # clip
        self.width, self.height = 16, 17
        self.x, self.y = 8, 7  # 생성 위치

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX

        self.x = 8
        for i in range(0, 3):
            self.image.clip_draw(self.left, self.bottom + self.height * i, self.width, self.height,
                                 self.x - Move_locX, self.y + self.width * i)  # 처음 시작 땅
        for i in range(0, 68):
            self.x += 15
            for j in range(0, 3):
                self.image.clip_draw(self.left + 16, self.bottom + self.height * j, self.width, self.height,
                                     self.x - Move_locX, self.y + self.width * j)  # 중간 땅
        self.x += 15
        for i in range(0, 3):
            self.image.clip_draw(self.left + 33, self.bottom + self.height * i, self.width - 1, self.height,
                                 self.x - Move_locX, self.y + self.width * i)  # 끝 땅

        self.x += 60
        for i in range(0, 3):
            self.image.clip_draw(self.left, self.bottom + self.height * i, self.width, self.height,
                                 self.x - Move_locX, self.y + self.width * i)  # 처음 시작 땅
        for i in range(0, 15):
            self.x += 15
            for j in range(0, 3):
                self.image.clip_draw(self.left + 16, self.bottom + self.height * j, self.width, self.height,
                                     self.x - Move_locX, self.y + self.width * j)  # 중간 땅
        self.x += 15
        for i in range(0, 3):
            self.image.clip_draw(self.left + 33, self.bottom + self.height * i, self.width - 1, self.height,
                                 self.x - Move_locX, self.y + self.width * i)  # 끝 땅

        self.x += 60
        for i in range(0, 3):
            self.image.clip_draw(self.left, self.bottom + self.height * i, self.width, self.height,
                                 self.x - Move_locX, self.y + self.width * i)  # 처음 시작 땅
        for i in range(0, 80):
            self.x += 15
            for j in range(0, 3):
                self.image.clip_draw(self.left + 16, self.bottom + self.height * j, self.width, self.height,
                                     self.x - Move_locX, self.y + self.width * j)  # 중간 땅
        self.x += 15
        for i in range(0, 3):
            self.image.clip_draw(self.left + 33, self.bottom + self.height * i, self.width - 1, self.height,
                                 self.x - Move_locX, self.y + self.width * i)  # 끝 땅

        self.x += 60
        for i in range(0, 3):
            self.image.clip_draw(self.left, self.bottom + self.height * i, self.width, self.height,
                                 self.x - Move_locX, self.y + self.width * i)  # 처음 시작 땅
        for i in range(0, 61):
            self.x += 15
            for j in range(0, 3):
                self.image.clip_draw(self.left + 16, self.bottom + self.height * j, self.width, self.height,
                                     self.x - Move_locX, self.y + self.width * j)  # 중간 땅

class SmallPipe:
    image = None

    def __init__(self):
        if SmallPipe.image == None:
            SmallPipe.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(305, 490, 40, 50, 460 - Move_locX, 60)

        self.image.clip_draw(305, 490, 40, 50, 2850 - Move_locX, 60)

        self.image.clip_draw(305, 490, 40, 50, 3100 - Move_locX, 60)

class MidPipe:
    image = None

    def __init__(self):
        if MidPipe.image == None:
            MidPipe.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(265, 490, 40, 60, 600 - Move_locX, 65)