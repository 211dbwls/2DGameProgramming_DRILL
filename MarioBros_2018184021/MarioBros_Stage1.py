from pico2d import *

STAGE_WIDTH, STAGE_HEIGHT = 800, 600


class Background:  # 배경
    def __init__(self):
        self.image = load_image('Back.png')

    def draw(self):
        self.image.draw(400, 300)

class Ground:  # 땅
    def __init__(self):
        self.image = load_image('Ground.png')
        self.left, self.bottom = 2, 155  # clip
        self.width, self.height = 16, 17
        self.x, self.y = 8, 7  # 생성 위치

    def draw(self):
        for i in range(0, 3):
            self.image.clip_draw(self.left, self.bottom + self.height * i, self.width, self.height,
                                 self.x, self.y + self.width * i)  # 처음 시작 땅

        for i in range(0, 54):
            for j in range(0, 3):
                self.image.clip_draw(self.left + 16, self.bottom + self.height * j, self.width, self.height,
                                     self.x + 15 * i, self.y + self.width * j)  # 중간 땅

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

class StartSign:  # 시작 표지판
    def __init__(self):
        self.image = load_image('Ground.png')
        self.left, self.bottom = 103, 64  # clip
        self.width, self.height = 17, 16
        self.x, self.y = 100, 56  # 생성 위치

    def draw(self):
        self.image.clip_draw(103, self.bottom, self.width, self.height, 100, self.y)
        self.image.clip_draw(120, self.bottom, self.width, self.height, 116, self.y)
        self.image.clip_draw(103, self.bottom + 17, self.width, self.height, 100, self.y + 16)
        self.image.clip_draw(120, self.bottom + 17, self.width, self.height, 116, self.y + 16)


class UpDownObstruction:
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw()


class QuestionBox:  # 물음표 상자
    def __init__(self):
        self.image = load_image('ItemsSheet.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 80, 30, 30, 250, 100)

class Coin:  # 코인
    def __init__(self):
        self.image = load_image('ItemsSheet.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정

    def draw(self):
        self.image.clip_draw(120 + self.frame * 30, 0, 30, 30, 200, 200)

class Brick:  # 벽돌
    def __init__(self):
        self.image = load_image('Ground.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(68, 36, 17, 16, 300, 107)

class Mario:  # 마리오
    def __init__(self):
        self.image = load_image('MarioAnimationSheet.png')
        self.left, self.bottom = 200, 170  # clip
        self.x, self.y = 20, 60  # 캐릭터 위치
        self.frame = 0  # 애니메이션 프레임
        self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = 0, 0, 0, 0, 0, 0
        self.t = 0  # 점프

    def update(self):  # 행위 구현
        global Mario_jumping

        if Mario_running == True:  # 이동 중일 경우 애니메이션 설정
            self.x += Mario_dir * 5  # 이동
            if Mario_dir == 1:  # 오른쪽으로 이동 중일 경우 애니메이션 설정
                self.left, self.bottom = 200, 170
                self.frame = (self.frame + 1) % 3
            elif Mario_dir == -1:  # 왼쪽으로 이동 중일 경우 애니메이션 설정
                self.left, self.bottom = 170, 170
                self.frame = -((self.frame + 1) % 3)

        if Mario_jumping == True:  # 점프 중일 경우 애니메이션 설정
            if Mario_right == True:  # 오른쪽 방향으로 점프할 경우
                if self.t == 0:  # 점프할 3점 위치 설정
                    self.x1, self.y1 = self.x, self.y  # 시작점
                    self.x2, self.y2 = self.x + 25, self.y + 50  # 중간점
                    self.x3, self.y3 = self.x + 50, self.y  # 끝점

                if self.t < 1:  # 세 점 곡선 그리기
                    self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.x1 + (
                            -4 * self.t ** 2 + 4 * self.t) * self.x2 + (2 * self.t ** 2 - self.t) * self.x3
                    self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.y1 + (
                            -4 * self.t ** 2 + 4 * self.t) * self.y2 + (2 * self.t ** 2 - self.t) * self.y3
                    self.frame = (self.frame + 1) % 6
                    self.t += 0.1
                elif self.t >= 1:  # 점프 끝나면 점프 종료
                    self.t = 0
                    Mario_jumping = False
            elif Mario_right == False:  # 왼쪽 방향으로 점프할 경우
                if self.t == 0:  # 점프할 3점 위치 설정
                    self.x1, self.y1 = self.x, self.y  # 시작점
                    self.x2, self.y2 = self.x - 25, self.y + 50  # 중간점
                    self.x3, self.y3 = self.x - 50, self.y  # 끝점

                if self.t <= 0 and self.t != -1:  # 세 점 곡선 그리기
                    self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.x1 + (
                                -4 * self.t ** 2 + 4 * self.t) * self.x2 + (2 * self.t ** 2 - self.t) * self.x3
                    self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.y1 + (
                                -4 * self.t ** 2 + 4 * self.t) * self.y2 + (2 * self.t ** 2 - self.t) * self.y3
                    self.t -= 0.1
                    self.frame = -((self.frame + 1) % 6)
                elif self.t <= -1:  # 점프 끝나면 점프 종료
                    self.t = 0
                    Mario_jumping = False


            # if Mario_dir == 1:  # 오른쪽 방향으로 점프하는 경우 애니메이션 설정
            #     self.left, self.bottom = 200, 170
            #     self.frame = (self.frame + 1) % 6
            #     self.y += 5
            # elif Mario_dir == -1:  # 왼쪽 방향으로 점프하는 경우 애니메이션 설정
            #     self.left, self.bottom =
            #     self.frame

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, 30, 30, self.x, self.y)


def handle_event():  # 입력처리
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


# initialization code : 초기화
open_canvas()

background = Background()  # 배경 생성
ground = Ground()  # 땅 생성
startsign = StartSign()  # 시작 표지판 생성
questionbox = QuestionBox()  # 물음표 상자 생성
coin = Coin()  # 코인 생성
brick = Brick()  # 벽돌 생성
character = Mario()  # 캐릭터 생성

# 변수
playing = True
Mario_running = False
Mario_jumping = False
Mario_sliding = False
Mario_right = True
Mario_dir = 0

while playing:
    handle_event()  # 키 입력 처리

    # Game Logic


    # Game Drawing
    clear_canvas()

    character.update()
    coin.update()

    background.draw()
    ground.draw()
    startsign.draw()
    questionbox.draw()
    brick.draw()
    coin.draw()
    character.draw()

    update_canvas()

    delay(0.05)

clear_canvas()


