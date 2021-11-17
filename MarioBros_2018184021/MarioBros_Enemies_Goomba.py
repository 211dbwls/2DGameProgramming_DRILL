from pico2d import *

class Goomba:  # 굼바
    image = None

    def __init__(self, left, bottom, width, height, x, y):
        if Goomba.image == None:
            Goomba.image = load_image('EnemiesAnimationSheet.png')

        self.left, self.bottom = left, bottom  # clip
        self.width, self.height = width, height
        self.x, self.y = x, y  # 생성 위치

        self.movex = 0
        self.frame = 0  # 애니메이션 프레임
        self.dir = 1  # 움직이는 방향 체크

    def get_bb(self):
        from MarioBros_Mario import Move_locX
        return self.x + self.movex - Move_locX - 17, self.y - 15, self.x + self.movex - Move_locX + 2, self.y + 10

    def dead(self):
        self.left, self.frame = 60, 0
        self.dir = 0

    def update(self):
        if self.dir == 1:  # 오른쪽 방향으로 이동
            self.movex += 2
            if self.movex == 50:
                self.dir = 1
            self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션
        elif self.dir == -1:  # 왼쪽 방향으로 이동
            self.movex -= 2
            if self.movex == 0:
                self.dir = -1
            self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left + self.frame * 30, self.bottom, self.width, self.height, self.x + self.movex - Move_locX, self.y)

        draw_rectangle(*self.get_bb())
