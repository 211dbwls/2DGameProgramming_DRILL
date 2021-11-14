from pico2d import *

import game_framework
import MarioBros_Stage1

name = "MarioBros_BonusStage"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------
background = None

lpipe = None
brick = None

coin = None

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

    def draw(self):
        for i in range(0, 48):
            for j in range(0, 3):
                self.image.clip_draw(392, 1112, 16, 17, 24 + 16 * i, 5 + 17 * j)

# 파이프, 벽돌 -----------------------------------------------------------------------------------------------------------
class LPipe:
    image = None

    def __init__(self):
        if LPipe.image == None:
            LPipe.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw(50, 500, 100, 130, 750, 110)

        self.image.clip_draw(70, 535, 80, 90, 760, 215)  # 위에 연결
        self.image.clip_draw(70, 535, 80, 90, 760, 305)
        self.image.clip_draw(70, 535, 80, 90, 760, 395)
        self.image.clip_draw(70, 535, 80, 90, 760, 485)

class Brick:  # 벽돌
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('ScenerySprites2.gif')

    def draw(self):
        for i in range(0, 3):
            for j in range(0, 30):
                self.image.clip_draw(393, 1134, 15, 16, 25 + 15 * i, 56 + 16 * j)

        for i in range(0, 22):
            for j in range(0, 5):
                self.image.clip_draw(393, 1134, 15, 16, 250 + 15 * i, 56 + 16 * j)

        for i in range(0, 22):
            for j in range(0, 3):
                self.image.clip_draw(393, 1134, 15, 16, 250 + 15 * i, 485 + 16 * j)

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
        for i in range(0, 11):
            for j in range(0, 2):
                self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 260 + 30 * i, 140 + 30 * j)

        for i in range(0, 9):
            self.image.clip_draw(120, 0, 30, 30, 400, 575)  # 코인 개수 이미지

            self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 260 + 30 * i + 30, 140 + 60)

# 플레이어 --------------------------------------------------------------------------------------------------------------
class Mario:  # 마리오
    image = None

    def __init__(self):
        if Mario.image == None:
            Mario.image = load_image('MarioAnimationSheet.png')

        self.left, self.bottom = 200, 170
        self.x, self.y = 90, 60  # 90
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
    global background, ground
    global lpipe, brick
    global coin
    global character

    global playing, Mario_running, Mario_jumping, Mario_sliding , Mario_right, Mario_dir, Move_locX

    # initialization code : 초기화
    background = Background()  # 배경 생성
    ground = Ground()  # 땅 생성

    lpipe = LPipe()  # 파이프 생성
    brick = Brick()  # 벽돌 생성

    coin = Coin()  # 코인 생성

    character = Mario()  # 캐릭터 생성

    playing = True
    Mario_running = False
    Mario_jumping = False
    Mario_sliding = False
    Mario_right = True
    Mario_dir = 0
    Move_locX = 0

def exit():
    global background, ground
    global lpipe, brick
    global coin
    global character

    del (background)
    del (ground)

    del (lpipe)
    del (brick)

    del (coin)

    del (character)

def update():
    character.update()

    coin.update()

def draw():
    clear_canvas()

    background.draw()
    ground.draw()

    lpipe.draw()
    brick.draw()

    coin.draw()

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


