from pico2d import *

class Goomba:  # 굼바
    image = None

    def __init__(self):
        if Goomba.image == None:
            Goomba.image = load_image('EnemiesAnimationSheet.png')

        self.movex = 0
        self.frame = 0  # 애니메이션 프레임
        self.right = True  # 움직이는 방향 체크

    def update(self):
        if self.right == True:  # 오른쪽 방향으로 이동
            self.movex += 2
            if self.movex == 50:
                self.right = False
        else:  # 왼쪽 방향으로 이동
            self.movex -= 2
            if self.movex == 0:
                self.right = True
        self.frame = (self.frame + 1) % 2  # 움직일 때 애니메이션

    def draw(self):
        from MarioBros_Mario import Move_locX

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 250 + self.movex - Move_locX, 60)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 785 + self.movex - Move_locX, 60)
        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 815 + self.movex - Move_locX, 60)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 1185 + self.movex - Move_locX, 127)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 1233 + self.movex - Move_locX, 177)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 1520 + self.movex - Move_locX, 60)
        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 1550 + self.movex - Move_locX, 60)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 1895 + self.movex - Move_locX, 60)
        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 1925 + self.movex - Move_locX, 60)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 2040 + self.movex - Move_locX, 60)
        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 2070 + self.movex - Move_locX, 60)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 2140 + self.movex - Move_locX, 60)
        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 2170 + self.movex - Move_locX, 60)

        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 2970 + self.movex - Move_locX, 60)
        self.image.clip_draw(0 + self.frame * 30, 240, 30, 30, 3000 + self.movex - Move_locX, 60)
