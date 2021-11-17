from pico2d import *

import game_framework
import game_world

import MarioBros_StartState
import MarioBros_BonusStage
import MarioBros_BossStage

from MarioBros_Stage1_Background import *
from MarioBros_Stage1_Background_Flag import *
from MarioBros_Stage1_Background_Castle import *
from MarioBros_Stage1_Background_Pipe import *
from MarioBros_Stage1_Background_Brick import *

from MarioBros_Enemies_Goomba import *
from MarioBros_Enemies_Flower import *
from MarioBros_Enemies_HammerBro import *

from MarioBros_Item_Coin import *
from MarioBros_Item_Star import *
from MarioBros_Item_QuestionBox import *

from MarioBros_Item_FireFlower import *
from MarioBros_Item_SuperMushroom import *
from MarioBros_Item_UpMushroom import *
from MarioBros_Item_PropellerMushroom import *

from MarioBros_Mario import *
from MarioBros_Mario_FireBall import *

name = "MarioBros_Stage1"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------
background = None
startsign = None
bigcloud = None
smallcloud = None
bigmountain = None
smallmountain = None
biggrass = None
smallgrass = None
collision_grounds = []
grounds = []

smallpipes = []
midpipe = None
largepipe = None
largepipe_bonus = None
brick = None

flag = None
castle = None

questionbox = None
coins = []
star = None
supermushroom = None
upmushroom = None
fireflower = None
propellermushroom = None

goombas = []
flower = None
hamerbro = None

mario = None
mario_fireball = None


# 함수 -----------------------------------------------------------------------------------------------------------------
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # 충돌이 안 일어나는 상황을 먼저 체크
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global background, startsign, bigcloud, smallcloud, bigmountain, smallmountain, biggrass, smallgrass
    global collision_grounds, grounds
    global smallpipes, midpipe, largepipe, largepipe_bonus, brick
    global flag, castle
    global questionbox, coins, star, supermushroom, upmushroom, fireflower, propellermushroom
    global goombas, flower, hamerbro
    global mario
    global mario_fireball

    # initialization code : 초기화
    background = Background()  # 배경 생성
    startsign = StartSign()  # 시작 표지판 생성
    bigcloud = BigCloud()  # 구름 생성
    smallcloud = SmallCloud()  # 구름 생성
    bigmountain = BigMountain()  # 산 생성
    smallmountain = SmallMountain()  # 산 생성
    biggrass = BigGrass()  # 풀 생성
    smallgrass = SmallGrass()  # 풀 생성
    # 땅 생성
    collision_grounds = [Ground(18, 155 + 34, 16, 17, 8 + 15 * i, 7 + 32) for i in range(0, 69)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 1035, 7 + 32)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 1095, 7 + 32)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 1110 + 15 * i, 7 + 32) for i in range(0, 15)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 1335, 7 + 32)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 1395, 7 + 32)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 1410 + 15 * i, 7 + 32) for i in range(0, 80)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 2610, 7 + 32)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 2670, 7 + 32)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 2685 + 15 * i, 7 + 32) for i in range(0, 61)]
    grounds = [Ground(18, 155, 16, 17, 8 + 15 * i, 7) for i in range(0, 69)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 15 * i, 7 + 16) for i in range(0, 69)] \
              + [Ground(35, 155, 15, 17, 8 + 1035, 7)] \
              + [Ground(35, 155 + 17, 15, 17, 8 + 1035, 7 + 16)] \
              + [Ground(2, 155, 16, 17, 8 + 1095, 7)] \
              + [Ground(2, 155 + 17, 16, 17, 8 + 1095, 7 + 16)] \
              + [Ground(18, 155, 16, 17, 8 + 1110 + 15 * i, 7) for i in range(0, 15)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 1110 + 15 * i, 7 + 16) for i in range(0, 15)] \
              + [Ground(35, 155, 15, 17, 8 + 1335, 7)] \
              + [Ground(35, 155 + 17, 15, 17, 8 + 1335, 7 + 16)] \
              + [Ground(2, 155, 16, 17, 8 + 1395, 7)] \
              + [Ground(2, 155 + 17, 16, 17, 8 + 1395, 7 + 16)] \
              + [Ground(18, 155, 16, 17, 8 + 1410 + 15 * i, 7) for i in range(0, 80)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 1410 + 15 * i, 7 + 16) for i in range(0, 80)] \
              + [Ground(35, 155, 15, 17, 8 + 2610, 7)] \
              + [Ground(35, 155 + 17, 15, 17, 8 + 2610, 7 + 16)] \
              + [Ground(2, 155, 16, 17, 8 + 2670, 7)] \
              + [Ground(2, 155 + 17, 16, 17, 8 + 2670, 7 + 16)] \
              + [Ground(18, 155, 16, 17, 8 + 2685 + 15 * i, 7) for i in range(0, 61)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 2685 + 15 * i, 7 + 16) for i in range(0, 61)]

    smallpipes = [SmallPipe(305, 490, 40, 50, 460, 60),
                  SmallPipe(305, 490, 40, 50, 2850, 60),
                  SmallPipe(305, 490, 40, 50, 3100, 60)]  # 파이프 생성

    midpipe = MidPipe(265, 490, 40, 60, 600, 65)  # 파이프 생성
    largepipe = LargePipe(225, 490, 40, 80, 740, 75)  # 파이프 생성
    largepipe_bonus = LargePipe(225, 490, 40, 80, 900, 75)  # 파이프 생성_보너스 맵 연결
    brick = Brick()  # 벽돌 생성

    flag = Flag()  # 깃발 생성
    castle = Castle()  # 성 생성

    questionbox = QuestionBox()  # 물음표 상자 생성
    # 코인 생성
    coins = [Coin(120, 0, 30, 30, 250, 130), Coin(120, 0, 30, 30, 335, 130), Coin(120, 0, 30, 30, 351, 130),
             Coin(120, 0, 30, 30, 1504, 130), Coin(120, 0, 30, 30, 1504, 130 + 50),
             Coin(120, 0, 30, 30, 1770, 130), Coin(120, 0, 30, 30, 1820, 130), Coin(120, 0, 30, 30, 1870, 130),
             Coin(120, 0, 30, 30, 2169, 130 + 50), Coin(120, 0, 30, 30, 2185, 130 + 50),
             Coin(120, 0, 30, 30, 2935, 130)]

    star = Star()  # 별 생성
    supermushroom = SuperMushroom()  # 슈퍼 버섯 생성
    upmushroom = UpMushroom()  # 업 버섯 생성
    fireflower = FireFlower()  # 파이어 플라워 생성
    propellermushroom = PropellerMushroom()  # 프로펠러 버섯 생성

    goombas = [Goomba(0, 240, 30, 30, 250, 60),
               Goomba(0, 240, 30, 30, 785, 60), Goomba(0, 240, 30, 30, 815, 60),
               Goomba(0, 240, 30, 30, 1185, 127),
               Goomba(0, 240, 30, 30, 1233, 177),
               Goomba(0, 240, 30, 30, 1520, 60), Goomba(0, 240, 30, 30, 1550, 60),
               Goomba(0, 240, 30, 30, 1895, 60), Goomba(0, 240, 30, 30, 1925, 60),
               Goomba(0, 240, 30, 30, 2040, 60), Goomba(0, 240, 30, 30, 2070, 60),
               Goomba(0, 240, 30, 30, 2140, 60), Goomba(0, 240, 30, 30, 2170, 60),
               Goomba(0, 240, 30, 30, 2970, 60), Goomba(0, 240, 30, 30, 3000, 60),
               Goomba(0, 240, 30, 30, 1895, 60), Goomba(0, 240, 30, 30, 1925, 60),]  # 굼바 생성

    flower = Flower()  # 플라워 생성
    hamerbro = HamerBro()  # 해머브러스 생성

    mario = Mario(900, 100)  # 캐릭터 생성

    game_world.add_object(background, 0)
    game_world.add_object(startsign, 0)
    game_world.add_object(bigcloud, 0)
    game_world.add_object(smallcloud, 0)
    game_world.add_object(bigmountain, 0)
    game_world.add_object(smallmountain, 0)
    game_world.add_object(biggrass, 0)
    game_world.add_object(smallgrass, 0)
    for collision_ground in collision_grounds:
        game_world.add_object(collision_ground, 0)
    for ground in grounds:
        game_world.add_object(ground, 0)

    for smallpipe in smallpipes:
        game_world.add_object(smallpipe, 0)
    game_world.add_object(midpipe, 0)
    game_world.add_object(largepipe, 0)
    game_world.add_object(largepipe_bonus, 0)
    game_world.add_object(brick, 0)

    game_world.add_object(flag, 0)
    game_world.add_object(castle, 0)

    game_world.add_object(questionbox, 0)
    for coin in coins:
        game_world.add_object(coin, 0)
    game_world.add_object(star, 0)
    game_world.add_object(supermushroom, 0)
    game_world.add_object(upmushroom, 0)
    game_world.add_object(fireflower, 0)
    game_world.add_object(propellermushroom, 0)

    for goomba in goombas:
        game_world.add_object(goomba, 0)
    game_world.add_object(flower, 0)
    game_world.add_object(hamerbro, 0)

    game_world.add_object(mario, 1)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 충돌 체크 및 충돌 처리
    # 마리오 - 땅
    ground_collision = False
    for collision_ground in collision_grounds:
        if collide(collision_ground, mario):
            ground_collision = True
    if ground_collision == True:
        mario.stop()
    else:
        mario.fall()

    # 마리오 - 코인
    for coin in coins:
        if collide(coin, mario):  # 코인과 충돌했을 경우
            mario.addCoin()  # 획득 코인 수 추가
            mario.addScore(200)  # 점수 추가
            coins.remove(coin)  # 코인 충돌 검사하는 리스트에서 제거
            game_world.remove_object(coin)  # 충돌한 코인 삭제

    # 마리오 - 파이프
    for smallpipe in smallpipes:
        if collide(smallpipe, mario):  # 파이프와 충돌했을 경우
            mario.cantgo()  # 앞으로 못 감
            mario.stop()
    if collide(midpipe, mario):
        mario.cantgo()
        mario.stop()
    if collide(largepipe, mario):
        mario.cantgo()
        mario.stop()
    if collide(largepipe_bonus, mario):  # 보너스맵과 연결된 파이프
        from MarioBros_Mario import Mario_in_BonusStage
        global Mario_in_BonusStage
        Mario_in_BonusStage = True
        game_framework.change_state(MarioBros_BonusStage)   # 보너스 맵으로 이동

    # 마리오 - 굼바
    for goomba in goombas:
        if collide(goomba, mario):  # 굼바와 충돌했을 경우
            goomba.dead()  # 굼바 죽음
            goombas.remove(goomba)  # 죽었을 경우 충돌 검사하는 리스트에서 제거
            game_world.remove_object(goomba)  # 충돌한 굼바 삭제
            mario.addScore(100)  # 점수 추가



def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    font = load_font('SuperMario256.ttf', 16)
    numfont = load_font('SuperMario256.ttf', 18)

    from MarioBros_Mario import Mario_score
    font.draw(30, 570, 'MARIO', (255, 255, 255))
    numfont.draw(100, 570, '%06d' % Mario_score, (255, 255, 255))

    from MarioBros_Mario import Mario_coins
    numfont.draw(405, 569, 'x', (255, 255, 255))
    numfont.draw(420, 569, '%02d' % Mario_coins, (255, 255, 255))

    font.draw(660, 570, 'TIME', (255, 255, 255))
    numfont.draw(720, 570, '%3.0f' % (400 - get_time()), (255, 255, 255))

    update_canvas()
    delay(0.07)

def handle_events():  # 입력처리
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 종료 버튼
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # esc키
            game_framework.change_state(MarioBros_StartState)  # 이전 화면으로 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_TAB:  # tab키
            game_framework.change_state(MarioBros_BossStage)  # 보스 스테이지 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:  # b키
            mario.changeBigMario()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:  # f키
            mario.changeFireMario()
        else:
            mario.handle_event(event)
