from pico2d import *

import game_framework
import MarioBros_Stage1

name = "MarioBros_BossStage"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------
background = None
ground = None
fireground = None
bridgeground = None

brick = None

coin = None

boss = None

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
        for i in range(0, 20):
            self.image.clip_draw(580, 770, 25, 15, self.x + 18 * i - Move_locX, 107)

        self.image.clip_draw(140, 1200, 40, 10, 2700 - Move_locX, 157)

class Brick:  # 벽돌
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('ScenerySprites2.gif')

    def draw(self):
        self.image.clip_draw(373, 1095, 16, 17, 968 - Move_locX, 264)

        self.image.clip_draw(373, 1095, 16, 17, 1180 - Move_locX, 264)

        self.image.clip_draw(373, 1095, 16, 17, 1416 - Move_locX, 264)
        self.image.clip_draw(373, 1095, 16, 17, 1630 - Move_locX, 264)
        self.image.clip_draw(373, 1095, 16, 17, 1844 - Move_locX, 264)
        self.image.clip_draw(373, 1095, 16, 17, 2058 - Move_locX, 264)

# 아이템 ----------------------------------------------------------------------------------------------------------------
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
        self.image.clip_draw(120, 0, 30, 30, 400, 575)  # 코인 개수 이미지
        #  self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 260 + 30 * i, 140 + 30 * j)

# 보스 ------------------------------------------------------------------------------------------------------------------
class Boss:  # 코인
    image = None

    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image('EnemiesAnimationSheet.png')

        self.frame = 0
        self.time = 0  # update 시간 조절

    def update(self):
        pass
        #if self.time % 2 == 0:
        #    self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정
        #self.time += 1

    def draw(self):
        self.image.clip_draw(0, 10, 40, 50, 2820 - Move_locX, 130)

# 플레이어 --------------------------------------------------------------------------------------------------------------
class Mario:  # 마리오
    image = None

    def __init__(self):
        if Mario.image == None:
            Mario.image = load_image('MarioAnimationSheet.png')

        self.left, self.bottom = 200, 170
        self.x, self.y = 2800, 125  # 30, 230 | 125 /// 2200
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
        if self.x >= 2900:  # 일정 거리를 넘으면 맵이 움직이지 않도록
            Move_locX = 2900 - 400

    def draw(self):
        print(self.x)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, 30, 30, self.x - Move_locX, self.y)

# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    global background, ground, fireground, bridgeground
    global brick
    global coin
    global boss
    global character

    global playing, Mario_running, Mario_jumping, Mario_sliding , Mario_right, Mario_dir, Move_locX

    # initialization code : 초기화
    background = Background()  # 배경 생성
    ground = Ground()  # 땅 생성
    fireground = FireGround()  # 불 생성
    bridgeground = BridgeGround()  # 다리 생성

    brick = Brick()  # 벽돌 생성

    coin = Coin()  # 코인 생성

    boss = Boss()  # 보스 생성

    character = Mario()  # 캐릭터 생성

    playing = True
    Mario_running = False
    Mario_jumping = False
    Mario_sliding = False
    Mario_right = True
    Mario_dir = 0
    Move_locX = 0

def exit():
    global background, ground, fireground, bridgeground
    global brick
    global coin
    global boss
    global character

    del (background)
    del (ground)
    del (fireground)
    del (bridgeground)

    del (brick)

    del (coin)

    del (boss)

    del (character)

def update():
    character.update()

    coin.update()

    boss.update()

def draw():
    clear_canvas()

    background.draw()
    fireground.draw()
    ground.draw()
    bridgeground.draw()

    brick.draw()

    coin.draw()

    boss.draw()

    character.draw()

    font = load_font('SuperMario256.ttf', 16)
    numfont = load_font('SuperMario256.ttf', 18)

    font.draw(30, 570, 'MARIO', (255, 255, 255))

    numfont.draw(100, 570, '000000', (255, 255, 255))

    numfont.draw(405, 569, 'x', (255, 255, 255))
    numfont.draw(420, 569, '00', (255, 255, 255))

    font.draw(660, 570, 'TIME', (255, 255, 255))
    numfont.draw(720, 570, '%3.0f' % (400 - get_time()), (255, 255, 255))

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
            game_framework.change_state(MarioBros_Stage1)  # 이전 화면으로 이동
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


