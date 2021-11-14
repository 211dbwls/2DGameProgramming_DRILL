from pico2d import *

playing = True
Mario_running = False
Mario_jumping = False
Mario_sliding = False
Mario_right = True
Mario_dir = 0
Move_locX = 0

class Mario:  # 마리오
    image = None

    def __init__(self, Start_locX, Start_locY):
        if Mario.image == None:
            Mario.image = load_image('MarioAnimationSheet.png')

        self.left, self.bottom = 200, 170
        self.width, self.height = 30, 30
        self.move_right_frame, self.move_left_frame = 200, 170
        self.x, self.y = Start_locX, Start_locY  # 30
        self.frame = 0  # 애니메이션 프레임
        self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = 0, 0, 0, 0, 0, 0  # 점프 시, 세 점
        self.t = 0  # 점프

    def changeBigMario(self):  # 큰 마리오
        self.bottom = 100
        self.height = 35

    def changeFireMario(self):  # 불 마리오
        self.bottom = 30
        self.width, self.height = 25, 35
        self.move_right_frame, self.move_left_frame = 230, 175

    def update(self):  # 행위 구현
        global Mario_jumping
        global Move_locX

        if Mario_running == True:  # 이동 중일 경우
            self.x += Mario_dir * 5  # 이동
            if Mario_dir == 1:  # 오른쪽으로 이동 중일 경우 애니메이션 설정
                self.left = self.move_right_frame
                self.frame = (self.frame + 1) % 3
            elif Mario_dir == -1:  # 왼쪽으로 이동 중일 경우 애니메이션 설정
                self.left = self.move_left_frame
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
        self.image.clip_draw(self.left + self.frame * self.width, self.bottom, self.width, self.height, self.x - Move_locX, self.y)

    def handle_events(self, event):  # 입력처리
        global playingaa
        global Mario_running
        global Mario_jumping
        global Mario_sliding
        global Mario_right
        global Mario_dir

        if event.type == SDL_KEYDOWN:  # 키 눌렀을 때
            if event.key == SDLK_d:  # D키_오른쪽으로 이동
                Mario_running = True
                Mario_right = True
                Mario_dir += 1
            if event.key == SDLK_a:  # A키_왼쪽으로 이동
                Mario_running = True
                Mario_right = False
                Mario_dir -= 1
            if event.key == SDLK_w:  # W키_점프
                Mario_jumping = True
            if event.key == SDLK_s:  # S키_숙이기
                pass
        elif event.type == SDL_KEYUP:  # 키 뗐을 때
            if event.key == SDLK_d:  # D키_앞으로 이동
                Mario_running = False
                Mario_dir -= 1
            if event.key == SDLK_a:  # A키_왼쪽으로 이동
                Mario_running = False
                Mario_dir += 1
            if event.key == SDLK_s:  # S키_숙이기
                pass
