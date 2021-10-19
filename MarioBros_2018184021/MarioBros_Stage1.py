from pico2d import *

STAGE_WIDTH, STAGE_HEIGHT = 800, 600

class Background:  # 배경
    def __init__(self):
        self.image = load_image('Back.png')

    def draw(self):
        self.image.draw(400, 300)

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

class Ground:  # 땅
    def __init__(self):
        self.image = load_image('Ground.png')
        self.left, self.bottom = 2, 155  # clip
        self.width, self.height = 16, 17
        self.x, self.y = 8, 7  # 생성 위치

    def draw(self):
        self.x = 8
        for i in range(0, 3):
            self.image.clip_draw(self.left, self.bottom + self.height * i, self.width, self.height,
                                 self.x, self.y + self.width * i)  # 처음 시작 땅

        for i in range(0, 30):
            self.x += 15
            for j in range(0, 3):
                self.image.clip_draw(self.left + 16, self.bottom + self.height * j, self.width, self.height,
                                     self.x, self.y + self.width * j)  # 중간 땅

        self.x += 15
        for i in range(0, 3):
            self.image.clip_draw(self.left + 33, self.bottom + self.height * i, self.width - 1, self.height,
                                 self.x, self.y + self.width * i)  # 끝 땅

        # 한 칸 위로
        self.x += 5
        for i in range(0, 4):
            self.image.clip_draw(self.left, self.bottom + self.height, self.width, self.height,
                                 self.x, self.y + self.width * i)
        self.image.clip_draw(self.left, self.bottom + self.height * 2, self.width, self.height,
                             self.x, self.y + self.width * 4)  # 시작 땅

        for i in range(0, 3):
            self.x += 15
            for j in range(0, 4):
                self.image.clip_draw(self.left + 16, self.bottom + self.height, self.width, self.height,
                                     self.x, self.y + self.width * j)
            self.image.clip_draw(self.left + 16, self.bottom + self.height * 2, self.width, self.height,
                                 self.x, self.y + self.width * 4)  # 중간 땅

        self.x += 15
        for i in range(0, 4):
            self.image.clip_draw(self.left + 33, self.bottom + self.height, self.width - 1, self.height,
                                 self.x, self.y + self.width * i)  # 끝 땅
        self.image.clip_draw(self.left + 33, self.bottom + self.height * 2, self.width, self.height,
                             self.x, self.y + self.width * 4)  # 끝 땅


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

class UpDownObstruction:  # 위아래로 움직이는 장애물
    def __init__(self):
        self.image = load_image('ScenerySprites.gif')

    def draw(self):
        self.image.clip_draw()

class Brick:  # 벽돌
    def __init__(self):
        self.image = load_image('Ground.png')
        self.left, self.bottom = 68, 36
        self.width, self.height = 17, 16
        self.x, self.y = 0, 0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 300, 107)
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, 332, 107)

class QuestionBox:  # 물음표 상자
    def __init__(self):
        self.image = load_image('ItemsSheet.png')
        self.left, self.bottom = 0, 80
        self.width, self.height = 30, 30
        self.x, self.y = 0, 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 3  # 제자리에서 색 변하도록 애니메이션 설정

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 250, 100)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 319, 100)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 319, 100 + 50)

class Coin:  # 코인
    def __init__(self):
        self.image = load_image('ItemsSheet.png')
        self.left, self.bottom = 120, 0
        self.width, self.height = 30, 30
        self.x, self.y = 0, 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 4  # 제자리에서 돌아가도록 애니메이션 설정

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 440, 80)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 460, 100)
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 480, 110)

class Star:  # 별
    def __init__(self):
        self.image = load_image('ItemsSheet.png')
        self.left, self.bottom = 0, 0
        self.width, self.height = 30, 30
        self.x, self.y = 0, 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 4  # 제자리에서 색 변하도록 애니메이션 설정

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, 200, 200)

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
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x, self.y)

class Flower:  # 플라워
    def __init__(self):
        self.image = load_image('EnemiesAnimationSheet.png')
        self.left, self.bottom = 380, 205  # clip
        self.width, self.height = 30, 30  # 크기
        self.x, self.y = 530, 90  # 위치
        self.frame = 0  # 애니메이션 프레임

    def update(self):
        self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x, self.y)

class HamerBro:  # 해머브러스
    def __init__(self):
        self.image = load_image('EnemiesAnimationSheet.png')
        self.left, self.bottom = 170, 145  # clip
        self.width, self.height = 30, 30  # 크기
        self.x, self.y = 450, 60  # 위치
        self.frame = 0  # 애니메이션 프레임
        self.right = True  # 움직이는 방향 체크

    def update(self):
        if self.right == True:  # 오른쪽 방향으로 이동
            self.x += 2
            if self.x == 550:
                self.left = 80
                self.right = False
        else:  # 왼쪽 방향으로  이동
            self.x -= 2
            if self.x == 450:
                self.left = 170
                self.right = True

        self.frame = (self.frame + 1) % 3  # 움직일 때 애니메이션

    def draw(self):
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x, self.y)


class Mario:  # 마리오
    def __init__(self):
        self.image = load_image('MarioAnimationSheet.png')
        self.left, self.bottom = 200, 170  # clip
        self.x, self.y = 20, 60  # 캐릭터 위치
        self.frame = 0  # 애니메이션 프레임
        self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = 0, 0, 0, 0, 0, 0  # 점프 시, 세 점
        self.t = 0  # 점프

    def update(self):  # 행위 구현
        global Mario_jumping

        if Mario_running == True:  # 이동 중일 경우
            self.x += Mario_dir * 5  # 이동
            if Mario_dir == 1:  # 오른쪽으로 이동 중일 경우 애니메이션 설정
                self.left, self.bottom = 200, 170
                self.frame = (self.frame + 1) % 3
            elif Mario_dir == -1:  # 왼쪽으로 이동 중일 경우 애니메이션 설정
                self.left, self.bottom = 170, 170
                self.frame = -((self.frame + 1) % 3)

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
startsign = StartSign()  # 시작 표지판 생성

ground = Ground()  # 땅 생성

brick = Brick()  # 벽돌 생성
questionbox = QuestionBox()  # 물음표 상자 생성
coin = Coin()  # 코인 생성
star = Star()  # 별 생성

goomba = Goomba()  # 굼바 생성
flower = Flower()  # 플라워 생성
hamerbro = HamerBro()  # 해머브러스 생성

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
    questionbox.update()
    coin.update()
    star.update()
    goomba.update()
    flower.update()
    hamerbro.update()

    background.draw()
    startsign.draw()
    ground.draw()
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

clear_canvas()


