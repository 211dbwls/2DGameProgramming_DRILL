from pico2d import *

class HamerBro:  # 해머브러스
    image = None

    def __init__(self):
        if HamerBro.image == None:
            HamerBro.image = load_image('EnemiesAnimationSheet.png')

        self.movex = 0
        self.left = 170
        self.frame = 0  # 애니메이션 프레임
        self.right = True  # 움직이는 방향 체크

        self.time = 0  # 공격 시간

    def update(self):
        if self.right == True:  # 오른쪽 방향으로 이동
            self.movex += 2
            if self.movex == 100:
                self.left = 80
                self.right = False
        else:  # 왼쪽 방향으로  이동
            self.movex -= 2
            if self.movex == 0:
                self.left = 170
                self.right = True

        self.frame = (self.frame + 1) % 3  # 움직일 때 애니메이션

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left + self.frame * 30, 145, 30, 30, 1700 + self.movex - Move_locX, 60)