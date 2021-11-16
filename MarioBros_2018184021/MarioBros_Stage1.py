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
ground = None

smallpipe = None
midpipe = None
largepipe = None
brick = None

flag = None
castle = None

questionbox = None
coin = None
star = None
supermushroom = None
upmushroom = None
fireflower = None
propellermushroom = None

goomba = None
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
    global background, startsign, bigcloud, smallcloud, bigmountain, smallmountain, biggrass, smallgrass, ground
    global smallpipe, midpipe, largepipe, brick
    global flag, castle
    global questionbox, coin, star, supermushroom, upmushroom, fireflower, propellermushroom
    global goomba, flower, hamerbro
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

    grounds = [Ground(18, 155, 16, 17, 8 + 15 * i, 7) for i in range(0, 69)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 15 * i, 7 + 16) for i in range(0, 69)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 15 * i, 7 + 32) for i in range(0, 69)] \
              + [Ground(35, 155, 15, 17, 8 + 1035, 7)] \
              + [Ground(35, 155 + 17, 15, 17, 8 + 1035, 7 + 16)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 1035, 7 + 32)] \
              + [Ground(2, 155, 16, 17, 8 + 1095, 7)] \
              + [Ground(2, 155 + 17, 16, 17, 8 + 1095, 7 + 16)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 1095, 7 + 32)] \
              + [Ground(18, 155, 16, 17, 8 + 1110 + 15 * i, 7) for i in range(0, 15)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 1110 + 15 * i, 7 + 16) for i in range(0, 15)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 1110 + 15 * i, 7 + 32) for i in range(0, 15)] \
              + [Ground(35, 155, 15, 17, 8 + 1335, 7)] \
              + [Ground(35, 155 + 17, 15, 17, 8 + 1335, 7 + 16)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 1335, 7 + 32)] \
              + [Ground(2, 155, 16, 17, 8 + 1395, 7)] \
              + [Ground(2, 155 + 17, 16, 17, 8 + 1395, 7 + 16)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 1395, 7 + 32)] \
              + [Ground(18, 155, 16, 17, 8 + 1410 + 15 * i, 7) for i in range(0, 80)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 1410 + 15 * i, 7 + 16) for i in range(0, 80)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 1410 + 15 * i, 7 + 32) for i in range(0, 80)] \
              + [Ground(35, 155, 15, 17, 8 + 2610, 7)] \
              + [Ground(35, 155 + 17, 15, 17, 8 + 2610, 7 + 16)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 2610, 7 + 32)] \
              + [Ground(2, 155, 16, 17, 8 + 2670, 7)] \
              + [Ground(2, 155 + 17, 16, 17, 8 + 2670, 7 + 16)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 2670, 7 + 32)] \
              + [Ground(18, 155, 16, 17, 8 + 2685 + 15 * i, 7) for i in range(0, 61)] \
              + [Ground(18, 155 + 17, 16, 17, 8 + 2685 + 15 * i, 7 + 16) for i in range(0, 61)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 2685 + 15 * i, 7 + 32) for i in range(0, 61)] \

    smallpipe = SmallPipe()  # 파이프 생성
    midpipe = MidPipe()  # 파이프 생성
    largepipe = LargePipe()  # 파이프 생성
    brick = Brick()  # 벽돌 생성

    flag = Flag()  # 깃발 생성
    castle = Castle()  # 성 생성

    questionbox = QuestionBox()  # 물음표 상자 생성
    coin = Coin()  # 코인 생성
    star = Star()  # 별 생성
    supermushroom = SuperMushroom()  # 슈퍼 버섯 생성
    upmushroom = UpMushroom()  # 업 버섯 생성
    fireflower = FireFlower()  # 파이어 플라워 생성
    propellermushroom = PropellerMushroom()  # 프로펠러 버섯 생성

    goomba = Goomba()  # 굼바 생성
    flower = Flower()  # 플라워 생성
    hamerbro = HamerBro()  # 해머브러스 생성

    mario = Mario(30, 100)  # 캐릭터 생성

    game_world.add_object(background, 0)
    game_world.add_object(startsign, 0)
    game_world.add_object(bigcloud, 0)
    game_world.add_object(smallcloud, 0)
    game_world.add_object(bigmountain, 0)
    game_world.add_object(smallmountain, 0)
    game_world.add_object(biggrass, 0)
    game_world.add_object(smallgrass, 0)
    for ground in grounds:
        game_world.add_object(ground, 0)

    game_world.add_object(smallpipe, 0)
    game_world.add_object(midpipe, 0)
    game_world.add_object(largepipe, 0)
    game_world.add_object(brick, 0)

    game_world.add_object(flag, 0)
    game_world.add_object(castle, 0)

    game_world.add_object(questionbox, 0)
    game_world.add_object(coin, 0)
    game_world.add_object(star, 0)
    game_world.add_object(supermushroom, 0)
    game_world.add_object(upmushroom, 0)
    game_world.add_object(fireflower, 0)
    game_world.add_object(propellermushroom, 0)

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
    if collide(ground, mario):
        mario.stop()

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 종료 버튼
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # esc키
            game_framework.change_state(MarioBros_StartState)  # 이전 화면으로 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:  # space키
            game_framework.change_state(MarioBros_BonusStage)  # 보너스 스테이지 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_TAB:  # tab키
            game_framework.change_state(MarioBros_BossStage)  # 보스 스테이지 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:  # b키
            mario.changeBigMario()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:  # f키
            mario.changeFireMario()
        else:
            mario.handle_event(event)
