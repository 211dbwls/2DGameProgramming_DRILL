from pico2d import *
import random

import game_framework
import game_world

from MarioBros_Mario_FireBall import FireBall

history = []  # (현재 상태, 이벤트) 저장하는 리스트

RIGHT_DOWN, LEFT_DOWN, JUMP_DOWN, RIGHT_UP, LEFT_UP, JUMP_UP, ENTER, DEBUG_KEY = range(8)

event_name = ['RIGHT_DOWN', 'LEFT_DOWN', 'JUMP_DOWN', 'RIGHT_UP', 'LEFT_UP', 'JUMP_UP', 'ENTER', 'DEBUG_KEY']

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_w): JUMP_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYUP, SDLK_w): JUMP_UP,
    (SDL_KEYUP, SDLK_l): ENTER,

    (SDL_KEYDOWN, SDLK_q): DEBUG_KEY
}

# 마리오 달리기 속도
MARIO_PIXEL_PER_METER = (10.0 / 0.3)  # 30 pixel 90 cm (1 pixel 3 cm)
MARIO_RUN_SPEED_KMPH = 20.0
MARIO_RUN_SPEED_MPM = (MARIO_RUN_SPEED_KMPH * 1000.0 / 60.0)
MARIO_RUN_SPEED_MPS = (MARIO_RUN_SPEED_MPM / 60.0)
MARIO_RUN_SPEED_PPS = (MARIO_RUN_SPEED_MPS * MARIO_PIXEL_PER_METER)

# 마리오 액션 속도
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3
FRAMES_PER_ACTION_JUMP = 6

jumping = False

Move_locX = 0

Mario_coins = 0
Mario_score = 0
Mario_life = 3

class IdleState:
    def enter(self, event):
        pass

    def exit(self, event):
        if event == ENTER:
            self.fire_ball()

    def do(self):
        pass

    def draw(self):
        self.image.clip_draw(self.left, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class RunState:
    def enter(self, event):
        if event == RIGHT_DOWN:
            self.velocity += MARIO_RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            self.velocity -= MARIO_RUN_SPEED_PPS
        elif event == RIGHT_UP:
            self.velocity -= MARIO_RUN_SPEED_PPS
        elif event == LEFT_UP:
            self.velocity += MARIO_RUN_SPEED_PPS

        self.dir = clamp(-1, self.velocity, 1)

    def exit(self, event):
        if event == ENTER:
            self.fire_ball()

    def do(self):
        if self.dir == 1:  # 오른쪽으로 이동 중일 경우 애니메이션 설정
            self.left = self.move_right_frame
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        elif self.dir == -1:  # 왼쪽으로 이동 중일 경우 애니메이션 설정
            self.left = self.move_left_frame
            self.frame = -((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3)
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(25, self.x, 3600)

    def draw(self):
        self.image.clip_draw(self.left + int(self.frame) * self.width, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

class JumpState:
    def enter(self, event):
        if self.jump_start == False:  # 점프할 3점 위치 설정
            if self.dir == 1:  # 오른쪽 방향으로 점프할 경우
                self.x1, self.y1 = self.x, self.y  # 시작점
                self.x2, self.y2 = self.x + 35, self.y + 50  # 중간점
                self.x3, self.y3 = self.x + 70, self.y  # 끝점
            elif self.dir == -1:  # 왼쪽 방향으로 점프할 경우
                self.x1, self.y1 = self.x, self.y  # 시작점
                self.x2, self.y2 = self.x - 35, self.y + 50  # 중간점
                self.x3, self.y3 = self.x - 70, self.y  # 끝점
            self.jump_start = True
            self.t = 0
        # if event == RIGHT_DOWN:
        #     self.velocity += MARIO_RUN_SPEED_PPS
        # elif event == LEFT_DOWN:
        #     self.velocity -= MARIO_RUN_SPEED_PPS
        # elif event == RIGHT_UP:
        #     self.velocity -= MARIO_RUN_SPEED_PPS
        # elif event == LEFT_UP:
        #     self.velocity += MARIO_RUN_SPEED_PPS
        #
        # self.dir = clamp(-1, self.velocity, 1)

    def exit(self, event):
        if event == ENTER:
            self.fire_ball()

    def do(self):
        # if self.dir == 1:  # 오른쪽으로 이동 중일 경우 애니메이션 설정
        #     self.left = self.move_right_frame
        #     self.frame = (self.frame + FRAMES_PER_ACTION_JUMP * ACTION_PER_TIME * game_framework.frame_time) % 6
        # elif self.dir == -1:  # 왼쪽으로 이동 중일 경우 애니메이션 설정
        #     self.left = self.move_left_frame
        #     self.frame = -((self.frame + FRAMES_PER_ACTION_JUMP * ACTION_PER_TIME * game_framework.frame_time) % 6)
        # self.x += self.velocity * game_framework.frame_time
        # self.x = clamp(25, self.x, 3600)
        #
        # self.y += self.gravity * game_framework.frame_time

        if self.t < 1:  # 세 점 곡선 그리기
            if self.dir == 1:  # 오른쪽 방향으로 점프할 경우
                self.frame = (self.frame + FRAMES_PER_ACTION_JUMP * ACTION_PER_TIME * game_framework.frame_time) % 6  # 애니메이션 설정
            elif self.dir == -1:  # 왼쪽 방향으로 점프할 경우
                self.frame = -((self.frame + FRAMES_PER_ACTION_JUMP * ACTION_PER_TIME * game_framework.frame_time) % 6)  # 애니메이션 설정

            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.x1 + (-4 * self.t ** 2 + 4 * self.t) * self.x2 + (
                    2 * self.t ** 2 - self.t) * self.x3
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.y1 + (-4 * self.t ** 2 + 4 * self.t) * self.y2 + (
                    2 * self.t ** 2 - self.t) * self.y3
            self.t += 0.1
        elif self.t >= 1:  # 점프 끝나면 점프 종료
            self.t = 0
            self.jump_start = False

    def draw(self):
        self.image.clip_draw(self.left + int(self.frame) * self.width, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, JUMP_UP: JumpState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState, JUMP_DOWN: JumpState, ENTER: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, JUMP_UP: JumpState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, JUMP_DOWN: JumpState, ENTER: RunState},
    JumpState: {RIGHT_UP: RunState, LEFT_UP: RunState, JUMP_UP: IdleState,
               LEFT_DOWN: RunState, RIGHT_DOWN: RunState, JUMP_DOWN: IdleState, ENTER: JumpState}
}

class Mario:  # 마리오
    image = None

    def __init__(self, Start_locX, Start_locY):
        if Mario.image == None:
            Mario.image = load_image('MarioAnimationSheet.png')

        self.left, self.bottom = 200, 170
        self.width, self.height = 30, 30

        self.x, self.y = Start_locX, Start_locY  # 30

        self.dir = 1
        self.velocity = 0  # 속도
        self.gravity = 9  # 중력

        self.move_right_frame, self.move_left_frame = 200, 170
        self.frame = 0  # 애니메이션 프레임

        self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = 0, 0, 0, 0, 0, 0  # 점프 시, 세 점
        self.t = 0  # 곡선 비율
        self.jump_start = False  # 점프

        self.event_que = []

        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.mario_in_bonusstage = False

    def changeBigMario(self):  # 큰 마리오
        self.bottom = 100
        self.height = 37
        self.y += 10

    def changeFireMario(self):  # 불 마리오
        self.bottom = 30
        self.width, self.height = 25, 37
        self.move_right_frame, self.move_left_frame = 230, 175

    def fire_ball(self):
        fireball = FireBall(self.x, self.y,  self.dir * 3)
        game_world.add_object(fireball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    # 충돌 체크
    def get_bb(self):
        return self.x - Move_locX - 10, self.y - 15, self.x - Move_locX + 10, self.y + 15

    def get_bb_foot(self):
        return self.x - Move_locX - 5, self.y - 15, self.x - Move_locX + 10, self.y - 5

    def get_bb_head(self):
        return self.x - Move_locX - 5, self.y + 10, self.x - Move_locX + 10, self.y + 15

    # 충돌처리 - 땅
    def stop(self, collide_loc):  # 땅과 충돌했을 경우 : 떨어지지 않도록
        global jumping
        if jumping == False:
            self.y = collide_loc

    def fall(self):  # 땅과 충돌하지 않았을 경우 : 떨어지도록
        global jumping
        if jumping == False:
            self.y -= self.gravity

    # 충돌 처리 - 코인 : 코인 개수 추가
    def addCoin(self):
        global Mario_coins
        Mario_coins += 1
    # 충돌 처리 - 점수 추가
    def addScore(self, score):
        global Mario_score
        Mario_score += score
    # 충돌 처리 - 목숨
    def addLife(self):
        global Mario_life
        Mario_life += 1
    def minusLife(self):
        global Mario_life
        Mario_life -= 1
    # 충돌 처리 - 작은 파이프 : 앞으로 못 가도록
    def cantgo_left(self, collide_loc):
        if self.x > collide_loc:
            self.x = collide_loc

    def cantgo_right(self, collide_loc):
        if self.x < collide_loc:
            self.x = collide_loc

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)  # 현재 상태 나감

            # error occurs here
            try:  # 시도를 해본다.
                history.append((self.cur_state.__name__, event_name[event]))  # (현재 상태, 이벤트) 튜플 저장
                self.cur_state = next_state_table[self.cur_state][event]
            except:  # 문제 발생 확인
                print('State : ' + self.cur_state.__name__ + ' event : ' + event_name[event])  # 현재 상태와 이벤트 출력
                exit(-1)

            self.cur_state.enter(self, event)  # 결정한 다음 상태 진행

    def draw(self):
        global Move_locX, Mario_in_BonusStage

        if self.mario_in_bonusstage == False:
            if self.x >= 400:  # 일정 거리를 넘으면 맵이 움직이도록
                Move_locX = self.x - 400
            if self.x >= 3200:  # 일정 거리를 넘으면 맵이 움직이지 않도록
                Move_locX = 3200 - 400
        else:
            Move_locX = 0

        self.cur_state.draw(self)

        debug_print('Velocity : ' + str(self.velocity) + ' Dir : ' + str(self.dir))

        print("Mario : " + str(self.x))

        # draw_rectangle(*self.get_bb())
        # draw_rectangle(*self.get_bb_foot())
        # draw_rectangle(*self.get_bb_head())

    def handle_event(self, event):
       if(event.type, event.key) in key_event_table:
           key_event = key_event_table[(event.type, event.key)]
           if DEBUG_KEY == key_event:  # history 출력_디버그
               print(history[-10:])
           else:
               self.add_event(key_event)
