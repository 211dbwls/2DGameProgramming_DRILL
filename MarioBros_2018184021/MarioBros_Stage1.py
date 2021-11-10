from pico2d import *

import game_framework
import MarioBros_StartState
import MarioBros_BonusStage

name = "MarioBros_Stage1"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------
background = None
startsign = None
bigcloud = None
smallcloud = None
bigmountain = None
smallmountain = None
biggrass = None
smallgrass = None
ground = None

smallpipe = None
midpipe = None
largepipe = None
brick = None

flag = None
castle = None

questionbox = None
coin = None
star = None
supermushroom = None
upmushroom = None
fireflower = None
propellermushroom = None

goomba = None
flower = None
hamerbro = None

character = None

playing = True
Mario_running = False
Mario_jumping = False
Mario_sliding = False
Mario_right = True
Mario_dir = 0
Move_locX = 0


# 배경 ------------------------------------------------------------------------------------------------------------------
class Background:  # 배경
    image = None

    def __init__(self):
        if Background.image == None:
            Background.image = load_image('Back.png')

    def draw(self):
        self.image.draw(400, 300)

class StartSign:  # 시작 표지판
    image = None

    def __init__(self):
        if StartSign.image == None:
            StartSign.image = load_image('GroundSheet.png')

    def draw(self):
        self.image.clip_draw(195, 90, 38, 55, 100 - Move_locX, 56)

class BigCloud:  # 구름
    image = None

    def __init__(self):
        if BigCloud.image == None:
            BigCloud.image = load_image('ScenerySprites.gif')

    def draw(self):
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

    def draw(self):
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

    def draw(self):
        self.image.clip_draw(80, 900, 90, 60, 180 - Move_locX, 60)

        self.image.clip_draw(80, 900, 90, 60, 800 - Move_locX, 60)

        self.image.clip_draw(80, 900, 90, 60, 1600 - Move_locX, 60)

        self.image.clip_draw(80, 900, 90, 60, 3300 - Move_locX, 60)

class SmallMountain:  # 산
    image = None

    def __init__(self):
        if SmallMountain.image == None:
            SmallMountain.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw(170, 900, 50, 60, 400 - Move_locX, 60)

        self.image.clip_draw(170, 900, 50, 60, 1000 - Move_locX, 60)

        self.image.clip_draw(170, 900, 50, 60, 1875 - Move_locX, 60)

        self.image.clip_draw(170, 900, 50, 60, 3560 - Move_locX, 60)

class BigGrass:  # 풀
    image = None

    def __init__(self):
        if BigGrass.image == None:
            BigGrass.image = load_image('ScenerySprites.gif')

    def draw(self):
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

    def draw(self):
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

    def draw(self):
        global Move_locX

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


# 파이프, 벽돌 -----------------------------------------------------------------------------------------------------------
class SmallPipe:
    image = None

    def __init__(self):
        if SmallPipe.image == None:
            SmallPipe.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw(305, 490, 40, 50, 460 - Move_locX, 60)

        self.image.clip_draw(305, 490, 40, 50, 2850 - Move_locX, 60)

        self.image.clip_draw(305, 490, 40, 50, 3100 - Move_locX, 60)

class MidPipe:
    image = None

    def __init__(self):
        if MidPipe.image == None:
            MidPipe.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw(265, 490, 40, 60, 600 - Move_locX, 65)

class LargePipe:
    image = None

    def __init__(self):
        if LargePipe.image == None:
            LargePipe.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw(225, 490, 40, 80, 740 - Move_locX, 75)

        self.image.clip_draw(225, 490, 40, 80, 900 - Move_locX, 75)  # 보너스 맵 연결

class Brick:  # 벽돌
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('Ground.png')

    def update(self):
        pass

    def draw(self):
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

# 깃발, 성 --------------------------------------------------------------------------------------------------------------
class Flag:
    image = None

    def __init__(self):
        if Flag.image == None:
            Flag.image = load_image('ScenerySprites.gif')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        pass
        #if self.time % 3 == 0:
        #    self.frame = (self.frame + 1) % 5  # 깃발 내려가도록
        #self.time += 1

    def draw(self):
        self.image.clip_draw(247 - self.frame * 33, 185, 25, 170, 3370 - Move_locX, 130)

class Castle:
    image = None

    def __init__(self):
        if Castle.image == None:
            Castle.image = load_image('ScenerySprites.gif')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(250, 0, 100, 100, 3500 - Move_locX, 90)

# 아이템 ----------------------------------------------------------------------------------------------------------------
class QuestionBox:  # 물음표 상자
    image = None

    def __init__(self):
        if QuestionBox.image == None:
            QuestionBox.image = load_image('ItemsSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 3  # 제자리에서 색 변하도록 애니메이션 설정
        self.time += 1

    def draw(self):
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 250 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 319 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 335 - Move_locX, 100 + 50)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 351 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 980 - Move_locX, 100 + 30)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1204 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1504 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1504 - Move_locX, 100 + 50)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1654 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1770 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1820 - Move_locX, 100)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1820 - Move_locX, 100 + 50)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 1870 - Move_locX, 100)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 2169 - Move_locX, 100 + 50)
        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 2185 - Move_locX, 100 + 50)

        self.image.clip_draw(0 + self.frame * 30, 80, 30, 30, 2935 - Move_locX, 100)

class Coin:  # 코인
    image = None

    def __init__(self):
        if Coin.image == None:
            Coin.image = load_image('ItemsSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 2 == 0:
            self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정
        self.time += 1

    def draw(self):
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 250 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 335 - Move_locX, 180)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 351 - Move_locX, 130)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1504 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1504 - Move_locX, 130 + 50)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1770 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1820 - Move_locX, 130)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 1870 - Move_locX, 130)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 2169 - Move_locX, 130 + 50)
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 2185 - Move_locX, 130 + 50)

        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 2935 - Move_locX, 130)

class Star:  # 별
    image = None

    def __init__(self):
        if Star.image == None:
            Star.image = load_image('ItemsSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 4  # 제자리에서 색 변하도록 애니메이션 설정
        self.time += 1

    def draw(self):
        self.image.clip_draw(0 + self.frame * 30, 0, 30, 30, 1654 - Move_locX, 130)

class SuperMushroom:  # 슈퍼 버섯 -> 키 커짐
    image = None

    def __init__(self):
        if SuperMushroom.image == None:
            SuperMushroom.image = load_image('ItemsSheet.png')

    def draw(self):
        self.image.clip_draw(180, 60, 30, 30, 319 - Move_locX, 127)


class UpMushroom:  # 1-UP 버섯 -> 목숨 + 1
    image = None

    def __init__(self):
        if UpMushroom.image == None:
            UpMushroom.image = load_image('ItemsSheet.png')

    def draw(self):
        self.image.clip_draw(210, 60, 30, 30, 1820 - Move_locX, 127 + 50)

class FireFlower:  # 파이어 플라워 -> 불 공격
    image = None

    def __init__(self):
        if FireFlower.image == None:
            FireFlower.image = load_image('ItemsSheet.png')

    def draw(self):
        self.image.clip_draw(140, 30, 30, 30, 1193 - Move_locX, 127)

class PropellerMushroom:  # 프로펠러 버섯 -> 날기 가능
    image = None

    def __init__(self):
        if PropellerMushroom.image == None:
            PropellerMushroom.image = load_image('ItemsSheet.png')

    def draw(self):
        pass
        #  self.image.clip_draw(0, 80, 30, 30, 250 - Move_locX, 100)


# 장애물 ----------------------------------------------------------------------------------------------------------------
class UpDownObstruction:  # 위아래로 움직이는 장애물
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw()

# 적군 ------------------------------------------------------------------------------------------------------------------
class Goomba:  # 굼바
    image = None

    def __init__(self):
        if Goomba.image == None:
            Goomba.image = load_image('EnemiesAnimationSheet.png')

        self.x, self.y = 250, 60  # 위치
        self.frame = 0  # 애니메이션 프레임
        self.right = True  # 움직이는 방향 체크

    def update(self):
        if self.right == True:  # 오른쪽 방향으로 이동
            self.x += 2
            if self.x == 350:
                self.right = False
        else:  # 왼쪽 방향으로 이동
            self.x -= 2
            if self.x == 250:
                self.right = True
        self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션

    def draw(self):
        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, self.x - Move_locX, self.y)

class Flower:  # 플라워
    image = None

    def __init__(self):
        if Flower.image == None:
            Flower.image = load_image('EnemiesAnimationSheet.png')

        self.frame = 0  # 애니메이션 프레임
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션
        self.time += 1

    def draw(self):
        pass
        # self.image.clip_draw(380 + self.frame * 30, 205, 30, 30, 600 - Move_locX, 60)

class HamerBro:  # 해머브러스
    image = None

    def __init__(self):
        if HamerBro.image == None:
            HamerBro.image = load_image('EnemiesAnimationSheet.png')

        self.x, self.y = 1000, 60  # 위치
        self.frame = 0  # 애니메이션 프레임
        self.right = True  # 움직이는 방향 체크

        self.time = 0  # 공격 시간

    def update(self):
        if self.right == True:  # 오른쪽 방향으로 이동
            self.x += 2
            if self.x == 1100:
                self.left = 80
                self.right = False
        else:  # 왼쪽 방향으로  이동
            self.x -= 2
            if self.x == 1000:
                self.left = 170
                self.right = True

        self.frame = (self.frame + 1) % 3  # 움직일 때 애니메이션

    def draw(self):
        pass
        # self.image.clip_draw(170 + self.frame * 30, 145, 30, 30, self.x - Move_locX, self.y)

# 플레이어 --------------------------------------------------------------------------------------------------------------
class Mario:  # 마리오
    image = None

    def __init__(self):
        if Mario.image == None:
            Mario.image = load_image('MarioAnimationSheet.png')

        self.left, self.bottom = 200, 170
        self.x, self.y = 1500, 60  # 30
        self.frame = 0  # 애니메이션 프레임
        self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = 0, 0, 0, 0, 0, 0  # 점프 시, 세 점
        self.t = 0  # 점프

    def update(self):  # 행위 구현
        global Mario_jumping
        global Move_locX

        if Mario_running == True:  # 이동 중일 경우
            self.x += Mario_dir * 5  # 이동
            if Mario_dir == 1:  # 오른쪽으로 이동 중일 경우 애니메이션 설정
                self.left, self.bottom = 200, 170
                self.frame = (self.frame + 1) % 3
            elif Mario_dir == -1:  # 왼쪽으로 이동 중일 경우 애니메이션 설정
                self.left, self.bottom = 170, 170
                self.frame = -((self.frame + 1) % 2)

        if Mario_jumping == True:  # 점프 중일 경우
            if self.t == 0:  # 점프할 3점 위치 설정
                if Mario_right == True:  # 오른쪽 방향으로 점프할 경우
                    self.x1, self.y1 = self.x, self.y  # 시작점
                    self.x2, self.y2 = self.x + 25, self.y + 50  # 중간점
                    self.x3, self.y3 = self.x + 50, self.y  # 끝점
                elif Mario_right == False:  # 왼쪽 방향으로 점프할 경우
                    self.x1, self.y1 = self.x, self.y  # 시작점
                    self.x2, self.y2 = self.x - 25, self.y + 50  # 중간점
                    self.x3, self.y3 = self.x - 50, self.y  # 끝점

            if self.t < 1:  # 세 점 곡선 그리기
                if Mario_right == True:  # 오른쪽 방향으로 점프할 경우
                    self.frame = (self.frame + 1) % 6  # 애니메이션 설정
                elif Mario_right == False:  # 왼쪽 방향으로 점프할 경우
                    self.frame = -((self.frame + 1) % 6)  # 애니메이션 설정

                self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.x1 + (
                        -4 * self.t ** 2 + 4 * self.t) * self.x2 + (2 * self.t ** 2 - self.t) * self.x3
                self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.y1 + (
                        -4 * self.t ** 2 + 4 * self.t) * self.y2 + (2 * self.t ** 2 - self.t) * self.y3
                self.t += 0.1
            elif self.t >= 1:  # 점프 끝나면 점프 종료
                self.t = 0
                Mario_jumping = False

        if self.x >= 400:  # 일정 거리를 넘으면 맵이 움직이도록
            Move_locX = self.x - 400
        if self.x >= 3200:  # 일정 거리를 넘으면 맵이 움직이지 않도록
            Move_locX = 3200 - 400

    def draw(self):
        print(self.x)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, 30, 30, self.x - Move_locX, self.y)


# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    global background, startsign, bigcloud, smallcloud, bigmountain, smallmountain, biggrass, smallgrass, ground
    global smallpipe, midpipe, largepipe, brick
    global flag, castle
    global questionbox, coin, star, supermushroom, upmushroom, fireflower, propellermushroom
    global goomba, flower, hamerbro
    global character

    global playing, Mario_running, Mario_jumping, Mario_sliding , Mario_right, Mario_dir, Move_locX

    # initialization code : 초기화
    background = Background()  # 배경 생성
    startsign = StartSign()  # 시작 표지판 생성
    bigcloud = BigCloud()  # 구름 생성
    smallcloud = SmallCloud()  # 구름 생성
    bigmountain = BigMountain()  # 산 생성
    smallmountain = SmallMountain()  # 산 생성
    biggrass = BigGrass()  # 풀 생성
    smallgrass = SmallGrass()  # 풀 생성
    ground = Ground()  # 땅 생성

    smallpipe = SmallPipe()  # 파이프 생성
    midpipe = MidPipe()  # 파이프 생성
    largepipe = LargePipe()  # 파이프 생성
    brick = Brick()  # 벽돌 생성

    flag = Flag()  # 깃발 생성
    castle = Castle()  # 성 생성

    questionbox = QuestionBox()  # 물음표 상자 생성
    coin = Coin()  # 코인 생성
    star = Star()  # 별 생성
    supermushroom = SuperMushroom()  # 슈퍼 버섯 생성
    upmushroom = UpMushroom()  # 업 버섯 생성
    fireflower = FireFlower()  # 파이어 플라워 생성
    propellermushroom = PropellerMushroom()  # 프로펠러 버섯 생성


    goomba = Goomba()  # 굼바 생성
    flower = Flower()  # 플라워 생성
    hamerbro = HamerBro()  # 해머브러스 생성

    character = Mario()  # 캐릭터 생성

    playing = True
    Mario_running = False
    Mario_jumping = False
    Mario_sliding = False
    Mario_right = True
    Mario_dir = 0
    Move_locX = 0

def exit():
    global background, startsign, bigcloud, smallcloud, bigmountain, smallmountain, biggrass, smallgrass, ground
    global smallpipe, midpipe, largepipe, brick
    global flag, castle
    global questionbox, coin, star, supermushroom, upmushroom, fireflower, propellermushroom
    global goomba, flower, hamerbro
    global character

    del (background)
    del (startsign)
    del (bigcloud)
    del (smallcloud)
    del (bigmountain)
    del (smallmountain)
    del (biggrass)
    del (smallgrass)
    del (ground)

    del (smallpipe)
    del (midpipe)
    del (largepipe)
    del (brick)

    del (flag)
    del (castle)

    del (questionbox)
    del (coin)
    del (star)
    del (supermushroom)
    del (upmushroom)
    del (fireflower)
    del (propellermushroom)

    del (goomba)
    del (flower)
    del (hamerbro)

    del (character)

def update():
    character.update()

    flag.update()
    castle.update()

    questionbox.update()
    coin.update()
    star.update()

    goomba.update()
    flower.update()
    hamerbro.update()

def draw():
    clear_canvas()

    background.draw()
    startsign.draw()
    bigcloud.draw()
    smallcloud.draw()
    bigmountain.draw()
    smallmountain.draw()
    biggrass.draw()
    smallgrass.draw()
    ground.draw()

    smallpipe.draw()
    midpipe.draw()
    largepipe.draw()
    brick.draw()

    flag.draw()
    castle.draw()

    questionbox.draw()
    coin.draw()
    star.draw()
    supermushroom.draw()
    upmushroom.draw()
    fireflower.draw()
    propellermushroom.draw()

    goomba.draw()
    flower.draw()
    hamerbro.draw()

    character.draw()

    update_canvas()
    delay(0.07)

def handle_events():  # 입력처리
    global playing
    global Mario_running
    global Mario_jumping
    global Mario_sliding
    global Mario_right
    global Mario_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 종료 버튼
            playing = False
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # esc키
            game_framework.change_state(MarioBros_StartState)  # 이전 화면으로 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:  # space키
            game_framework.change_state(MarioBros_BonusStage)  # 보너스 스테이지 이동
        elif event.type == SDL_KEYDOWN:  # 키 눌렀을 때
            if event.key == SDLK_d:  # D키_오른쪽으로 이동
                Mario_running = True
                Mario_right = True
                Mario_dir += 1
            if event.key == SDLK_a:   # A키_왼쪽으로 이동
                Mario_running = True
                Mario_right = False
                Mario_dir -= 1
            if event.key == SDLK_w:   # W키_점프
                Mario_jumping = True
            if event.key == SDLK_s:  # S키_숙이기
                pass
            if event.key == SDLK_ESCAPE:  # esc 키_종료
                playing = False
        elif event.type == SDL_KEYUP:  # 키 뗐을 때
            if event.key == SDLK_d:  # D키_앞으로 이동
                Mario_running = False
                Mario_dir -= 1
            if event.key == SDLK_a:   # A키_왼쪽으로 이동
                Mario_running = False
                Mario_dir += 1
            if event.key == SDLK_s:  # S키_숙이기
                pass


