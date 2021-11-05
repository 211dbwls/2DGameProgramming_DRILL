from pico2d import *

import game_framework
import MarioBros_StartState

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

questionbox = None
coin = None
star = None

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
    def __init__(self):
        self.image = load_image('Back.png')

    def draw(self):
        self.image.draw(400, 300)

class StartSign:  # 시작 표지판
    def __init__(self):
        self.image = load_image('GroundSheet.png')
        self.left, self.bottom = 195, 90  # clip
        self.width, self.height = 38, 55
        self.x, self.y = 100, 56  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class BigCloud:  # 구름
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 140, 850  # clip
        self.width, self.height = 70, 40
        self.x, self.y = 500, 300  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 550 - Move_locX, 300)

        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 900 - Move_locX, 350)

class SmallCloud:  # 구름
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 210, 855  # clip
        self.width, self.height = 35, 30
        self.x, self.y = 200, 300  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 200 - Move_locX, 300)
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 300 - Move_locX, 350)
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 650 - Move_locX, 350)

        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 1000 - Move_locX, 300)
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 1100 - Move_locX, 300)

class BigMountain:  # 산
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 80, 900  # clip
        self.width, self.height = 90, 60
        self.x, self.y = 200, 60  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 200 - Move_locX, self.y)

        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 1100- Move_locX, self.y)

class SmallMountain:  # 산
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 170, 900  # clip
        self.width, self.height = 50, 60
        self.x, self.y = 530, 60  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class BigGrass:  # 풀
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 220, 900  # clip
        self.width, self.height = 70, 60
        self.x, self.y = 400, 60  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class SmallGrass:  # 풀
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 290, 900  # clip
        self.width, self.height = 30, 60
        self.x, self.y = 565, 60  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 565 - Move_locX, self.y)

        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 700 - Move_locX, self.y)

class Ground:  # 땅
    def __init__(self):
        self.image = load_image('Ground.png')
        self.left, self.bottom = 2, 155  # clip
        self.width, self.height = 16, 17
        self.x, self.y = 8, 7  # 생성 위치

    def draw(self):
        global Move_locX

        self.x = 8
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

        # 한 칸 위로
        # self.x += 5
        # for i in range(0, 4):
        #     self.image.clip_draw(self.left, self.bottom + self.height, self.width, self.height,
        #                          self.x, self.y + self.width * i)
        # self.image.clip_draw(self.left, self.bottom + self.height * 2, self.width, self.height,
        #                      self.x, self.y + self.width * 4)  # 시작 땅
        #
        # for i in range(0, 3):
        #     self.x += 15
        #     for j in range(0, 4):
        #         self.image.clip_draw(self.left + 16, self.bottom + self.height, self.width, self.height,
        #                              self.x, self.y + self.width * j)
        #     self.image.clip_draw(self.left + 16, self.bottom + self.height * 2, self.width, self.height,
        #                          self.x, self.y + self.width * 4)  # 중간 땅
        #
        # self.x += 15
        # for i in range(0, 4):
        #     self.image.clip_draw(self.left + 33, self.bottom + self.height, self.width - 1, self.height,
        #                          self.x, self.y + self.width * i)  # 끝 땅
        # self.image.clip_draw(self.left + 33, self.bottom + self.height * 2, self.width, self.height,
        #                      self.x, self.y + self.width * 4)  # 끝 땅


        # for i in range(0, 3):
        #     self.image.clip_draw(self.left + 32, self.bottom + self.height * i, self.width, self.height,
        #                          self.x + 225, self.y + self.width * i)  # 끝 땅

        # 처음 시작 땅
        # self.image.clip_draw(2, 155, 16, 17, 8, 7)
        # self.image.clip_draw(2, 172, 16, 17, 8, 23)
        # self.image.clip_draw(2, 189, 16, 17, 8, 39)
        # 중간 땅
        # self.image.clip_draw(18(+16), 155, 16, 17, 23(+15), 7)
        # self.image.clip_draw(18(+16), 172, 16, 17, 23(+15), 23)
        # self.image.clip_draw(18(+16), 189, 16, 17, 23(+15), 39)

        # self.image.clip_draw(18, 155, 16, 17, 38(+15), 7)
        # self.image.clip_draw(18, 172, 16, 17, 38(+15), 23)
        # self.image.clip_draw(18, 189, 16, 17, 38(+15), 39)

# clip_draw(left, bottom, width, height, x, y)

# 파이프, 벽돌 -----------------------------------------------------------------------------------------------------------
class SmallPipe:
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 305, 490  # clip
        self.width, self.height = 40, 50
        self.x, self.y = 800, 60  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class MidPipe:
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 265, 490  # clip
        self.width, self.height = 40, 60
        self.x, self.y = 950, 65  # 생성 위치

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 950 - Move_locX, 65)

class LargePipe:
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')
        self.left, self.bottom = 300, 490  # clip
        self.width, self.height = 50, 50
        self.x, self.y = 800, 60  # 생성 위치

    def draw(self):
        pass
        # self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class Brick:  # 벽돌
    def __init__(self):
        self.image = load_image('Ground.png')
        self.left, self.bottom = 68, 36
        self.width, self.height = 17, 16
        self.x, self.y = 0, 0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 300 - Move_locX, 107)
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 332 - Move_locX, 107)

        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 660 - Move_locX, 107)
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 676 - Move_locX, 107)
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 692 - Move_locX, 107)

# 아이템 ----------------------------------------------------------------------------------------------------------------
class QuestionBox:  # 물음표 상자
    def __init__(self):
        self.image = load_image('ItemsSheet.png')
        self.left, self.bottom = 0, 80
        self.width, self.height = 30, 30
        self.x, self.y = 0, 0
        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 3  # 제자리에서 색 변하도록 애니메이션 설정
        self.time += 1

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 250 - Move_locX, 100)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 319 - Move_locX, 100)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 319 - Move_locX, 100 + 50)

class Coin:  # 코인
    def __init__(self):
        self.image = load_image('ItemsSheet.png')
        self.left, self.bottom = 120, 0
        self.width, self.height = 30, 30
        self.x, self.y = 0, 0
        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 2 == 0:
            self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정
        self.time += 1

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 440 - Move_locX, 60)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 460 - Move_locX, 60)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 480 - Move_locX, 60)

        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 662 - Move_locX, 130)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 678 - Move_locX, 130)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 694 - Move_locX, 130)

class Star:  # 별
    def __init__(self):
        self.image = load_image('ItemsSheet.png')
        self.left, self.bottom = 0, 0
        self.width, self.height = 30, 30
        self.x, self.y = 0, 0
        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 4  # 제자리에서 색 변하도록 애니메이션 설정
        self.time += 1

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 955 - Move_locX, 120)

# 장애물 ----------------------------------------------------------------------------------------------------------------
class UpDownObstruction:  # 위아래로 움직이는 장애물
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw()

# 적군 ------------------------------------------------------------------------------------------------------------------
class Goomba:  # 굼바
    def __init__(self):
        self.image = load_image('EnemiesAnimationSheet.png')
        self.left, self.bottom = 0, 240  # clip
        self.width, self.height = 30, 30  # 크기
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
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class Flower:  # 플라워
    def __init__(self):
        self.image = load_image('EnemiesAnimationSheet.png')
        self.left, self.bottom = 380, 205  # clip
        self.width, self.height = 30, 30  # 크기
        self.x, self.y = 600, 60  # 위치
        self.frame = 0  # 애니메이션 프레임
        self.time = 0  # update 시간 조절

    def update(self):
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션
        self.time += 1

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class HamerBro:  # 해머브러스
    def __init__(self):
        self.image = load_image('EnemiesAnimationSheet.png')
        self.left, self.bottom = 170, 145  # clip
        self.width, self.height = 30, 30  # 크기
        self.x, self.y = 1000, 60  # 위치
        self.frame = 0  # 애니메이션 프레임
        self.right = True  # 움직이는 방향 체크

        self.time = 0  # 공격 시간
        self.hammerimage = load_image('EnemiesAnimationSheet.png')
        # self.left, self.bottom = 170, 145  # clip
        # self.width, self.height = 30, 30  # 크기
        # self.x, self.y = 1000, 60  # 위치
        # self.frame = 0  # 애니메이션 프레임
        # self.right = True  # 움직이는 방향 체크

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
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

# 플레이어 --------------------------------------------------------------------------------------------------------------
class Mario:  # 마리오
    def __init__(self):
        self.image = load_image('MarioAnimationSheet.png')
        self.left, self.bottom = 200, 170  # clip
        self.x, self.y = 30, 60  # 캐릭터 위치 30
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
        if self.x >= 800:  # 일정 거리를 넘으면 맵이 움직이지 않도록
            Move_locX = 800 - 400

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, 30, 30, self.x - Move_locX, self.y)


# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    global background, startsign, bigcloud, smallcloud, bigmountain, smallmountain, biggrass, smallgrass, ground
    global smallpipe, midpipe, largepipe, brick
    global questionbox, coin, star
    global goomba, flower, hamerbro
    global character

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

    questionbox = QuestionBox()  # 물음표 상자 생성
    coin = Coin()  # 코인 생성
    star = Star()  # 별 생성

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
    global questionbox, coin, star
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

    del (questionbox)
    del (coin)
    del (star)

    del (goomba)
    del (flower)
    del (hamerbro)

    del (character)

def update():
    character.update()

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

    questionbox.draw()
    coin.draw()
    star.draw()

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


