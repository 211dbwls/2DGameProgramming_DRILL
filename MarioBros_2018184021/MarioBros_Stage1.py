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

# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    global background, startsign, bigcloud, smallcloud, bigmountain, smallmountain, biggrass, smallgrass, ground
    global smallpipe, midpipe, largepipe, brick
    global flag, castle
    global questionbox, coin, star, supermushroom, upmushroom, fireflower, propellermushroom
    global goomba, flower, hamerbro
    global mario

    global playing, Mario_running, Mario_jumping, Mario_sliding , Mario_right, Mario_dir, Move_locX

    # initialization code : 초기화
    background = Background()  # 배경 생성
    startsign = StartSign()  # 시작 표지판 생성
    bigcloud = BigCloud()  # 구름 생성
    smallcloud = SmallCloud()  # 구름 생성
    bigmountain = BigMountain()  # 산 생성
    smallmountain = SmallMountain()  # 산 생성
    biggrass = BigGrass()  # 풀 생성
    smallgrass = SmallGrass()  # 풀 생성
    ground = Ground()  # 땅 생성

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

    mario = Mario()  # 캐릭터 생성

def exit():
    global background, startsign, bigcloud, smallcloud, bigmountain, smallmountain, biggrass, smallgrass, ground
    global smallpipe, midpipe, largepipe, brick
    global flag, castle
    global questionbox, coin, star, supermushroom, upmushroom, fireflower, propellermushroom
    global goomba, flower, hamerbro
    global mario

    del (background)
    del (startsign)
    del (bigcloud)
    del (smallcloud)
    del (bigmountain)
    del (smallmountain)
    del (biggrass)
    del (smallgrass)
    del (ground)

    del (smallpipe)
    del (midpipe)
    del (largepipe)
    del (brick)

    del (flag)
    del (castle)

    del (questionbox)
    del (coin)
    del (star)
    del (supermushroom)
    del (upmushroom)
    del (fireflower)
    del (propellermushroom)

    del (goomba)
    del (flower)
    del (hamerbro)

    del (mario)

def update():
    mario.update()

    flag.update()
    castle.update()

    questionbox.update()
    coin.update()
    star.update()

    goomba.update()
    flower.update()
    hamerbro.update()

def draw():
    clear_canvas()

    background.draw()
    startsign.draw()
    bigcloud.draw()
    smallcloud.draw()
    bigmountain.draw()
    smallmountain.draw()
    biggrass.draw()
    smallgrass.draw()
    ground.draw()

    smallpipe.draw()
    midpipe.draw()
    largepipe.draw()
    brick.draw()

    flag.draw()
    castle.draw()

    questionbox.draw()
    coin.draw()
    star.draw()
    supermushroom.draw()
    upmushroom.draw()
    fireflower.draw()
    propellermushroom.draw()

    goomba.draw()
    flower.draw()
    hamerbro.draw()

    mario.draw()

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
        else:
            mario.handle_events(event)



