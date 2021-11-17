from pico2d import *
import game_world
from MarioBros_Enemies_HammerBro_Hammer import Hammer

class HamerBro:  # 해머브러스
    image = None

    def __init__(self):
        if HamerBro.image == None:
            HamerBro.image = load_image('EnemiesAnimationSheet.png')

        self.x, self.y = 1700, 60
        self.movex = 0
        self.left = 170
        self.frame = 0  # 애니메이션 프레임
        self.right = True  # 움직이는 방향 체크
        self.dir = 1
        self.time = 0  # 공격 시간

    def throw_hammer(self):
        hammer = Hammer(self.x, self.y, self.dir * 3)
        game_world.add_object(hammer, 1)

    def update(self):
        if self.right == True:  # 오른쪽 방향으로 이동
            self.movex += 2
            if self.movex == 100:
                self.left = 80
                self.right = False
                self.dir = -1
        else:  # 왼쪽 방향으로  이동
            self.movex -= 2
            if self.movex == 0:
                self.left = 170
                self.right = True
                self.dir = 1

        self.frame = (self.frame + 1) % 3  # 움직일 때 애니메이션

        if self.time % 3 == 0:
            self.throw_hammer()

        self.time += 1

    def draw(self):
        from MarioBros_Mario import Move_locX
        self.image.clip_draw(self.left + self.frame * 30, 145, 30, 30, 1700 + self.movex - Move_locX, 60)