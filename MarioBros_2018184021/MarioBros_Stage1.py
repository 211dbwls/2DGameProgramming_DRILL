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

import server
import collision

name = "MarioBros_Stage1"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------

# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    # initialization code : 초기화
    server.background = Background()  # 배경 생성
    server.startsign = StartSign()  # 시작 표지판 생성
    server.bigcloud = BigCloud()  # 구름 생성
    server.smallcloud = SmallCloud()  # 구름 생성
    server.bigmountain = BigMountain()  # 산 생성
    server.smallmountain = SmallMountain()  # 산 생성
    server.biggrass = BigGrass()  # 풀 생성
    server.smallgrass = SmallGrass()  # 풀 생성
    # 땅 생성
    server.collision_grounds = [Ground(18, 155 + 34, 16, 17, 8 + 15 * i, 7 + 32) for i in range(0, 69)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 1035, 7 + 32)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 1095, 7 + 32)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 1110 + 15 * i, 7 + 32) for i in range(0, 15)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 1335, 7 + 32)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 1395, 7 + 32)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 1410 + 15 * i, 7 + 32) for i in range(0, 80)] \
              + [Ground(35, 155 + 34, 15, 17, 8 + 2610, 7 + 32)] \
              + [Ground(2, 155 + 34, 16, 17, 8 + 2670, 7 + 32)] \
              + [Ground(18, 155 + 34, 16, 17, 8 + 2685 + 15 * i, 7 + 32) for i in range(0, 61)]
    server.grounds = [Ground(18, 155, 16, 17, 8 + 15 * i, 7) for i in range(0, 69)] \
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

    server.smallpipes = [SmallPipe(305, 490, 40, 50, 460, 60),
                  SmallPipe(305, 490, 40, 50, 2850, 60),
                  SmallPipe(305, 490, 40, 50, 3100, 60)]  # 파이프 생성

    server.midpipe = MidPipe(265, 490, 40, 60, 600, 65)  # 파이프 생성
    server.largepipe = LargePipe(225, 490, 40, 80, 740, 75)  # 파이프 생성
    server.largepipes_bonus = [LargePipe(225, 490, 40, 80, 900, 75)]  # 파이프 생성_보너스 맵 연결

    server.bricks = [Brick(68, 36, 17, 16, 300, 107), Brick(68, 36, 17, 16, 332, 107), Brick(68, 36, 17, 16, 364, 107)]  \
                   + [Brick(68, 36, 17, 16, 1185, 107), Brick(68, 36, 17, 16, 1217, 107)] \
                   + [Brick(68, 36, 17, 16, 1233 + i * 16, 107 + 50) for i in range(0, 10)] \
                   + [Brick(68, 36, 17, 16, 1453 + i * 16, 107 + 50) for i in range(0, 3)] \
                   + [Brick(68, 36, 17, 16, 1635, 107), Brick(68, 36, 17, 16, 1980, 107)] \
                   + [Brick(68, 36, 17, 16, 2050 + i * 16, 107 + 50) for i in range(0, 3)] \
                   + [Brick(68, 36, 17, 16, 2150, 107 + 50), Brick(68, 36, 17, 16, 2198, 107 + 50)] \
                   + [Brick(68, 36, 17, 16, 2169, 107), Brick(68, 36, 17, 16, 2185, 107)] \
                   + [Brick(68, 36, 17, 16, 2900, 107), Brick(68, 36, 17, 16, 2916, 107), Brick(68, 36, 17, 16, 2948, 107)]  # 벽돌 생성

    server.flag = Flag()  # 깃발 생성
    server.castle = Castle(250, 0, 100, 100, 3500, 90)  # 성 생성

    server.questionboxs_coin = [QuestionBox(0, 80, 30, 30, 250, 100),
                         QuestionBox(0, 80, 30, 30, 335, 100 + 50), QuestionBox(0, 80, 30, 30, 351, 100 + 50),
                         QuestionBox(0, 80, 30, 30, 1504, 100), QuestionBox(0, 80, 30, 30, 1504, 100 + 50),
                         QuestionBox(0, 80, 30, 30, 1770, 100), QuestionBox(0, 80, 30, 30, 1820, 100), QuestionBox(0, 80, 30, 30, 1870, 100),
                         QuestionBox(0, 80, 30, 30, 2169, 100 + 50), QuestionBox(0, 80, 30, 30, 2185, 100 + 50),
                         QuestionBox(0, 80, 30, 30, 2935, 100)]  # 물음표 상자_코인 생성

    server.questionboxs_star = [QuestionBox(0, 80, 30, 30, 1654, 100 + 50)]
    server.questionboxs_supermushroom = [QuestionBox(0, 80, 30, 30, 319, 100)]
    server.questionboxs_upmushroom = [QuestionBox(0, 80, 30, 30, 980, 100 + 30), QuestionBox(0, 80, 30, 30, 1820, 100 + 50)]
    server.questionboxs_fireflower = [QuestionBox(0, 80, 30, 30, 1204, 100)]
    # questionbox_propellermushroom

    server.goombas = [Goomba(0, 240, 30, 30, 250, 60),
               Goomba(0, 240, 30, 30, 785, 60), Goomba(0, 240, 30, 30, 815, 60),
               Goomba(0, 240, 30, 30, 1185, 127),
               Goomba(0, 240, 30, 30, 1233, 177),
               Goomba(0, 240, 30, 30, 1520, 60), Goomba(0, 240, 30, 30, 1550, 60),
               Goomba(0, 240, 30, 30, 1895, 60), Goomba(0, 240, 30, 30, 1925, 60),
               Goomba(0, 240, 30, 30, 2040, 60), Goomba(0, 240, 30, 30, 2070, 60),
               Goomba(0, 240, 30, 30, 2140, 60), Goomba(0, 240, 30, 30, 2170, 60),
               Goomba(0, 240, 30, 30, 2970, 60), Goomba(0, 240, 30, 30, 3000, 60),
               Goomba(0, 240, 30, 30, 1895, 60), Goomba(0, 240, 30, 30, 1925, 60)]  # 굼바 생성

    server.flower = Flower()  # 플라워 생성
    server.hamerbro = HamerBro()  # 해머브러스 생성

    server.mario = Mario(server.start_loc_x, server.start_loc_y)  # 캐릭터 생성
    # server.mario = Mario(30, 150)  # 캐릭터 생성

    game_world.add_object(server.background, 0)
    game_world.add_object(server.startsign, 0)
    game_world.add_object(server.bigcloud, 0)
    game_world.add_object(server.smallcloud, 0)
    game_world.add_object(server.bigmountain, 0)
    game_world.add_object(server.smallmountain, 0)
    game_world.add_object(server.biggrass, 0)
    game_world.add_object(server.smallgrass, 0)
    for collision_ground in server.collision_grounds:
        game_world.add_object(collision_ground, 0)
    for ground in server.grounds:
        game_world.add_object(ground, 0)

    for smallpipe in server.smallpipes:
        game_world.add_object(smallpipe, 0)
    game_world.add_object(server.midpipe, 0)
    game_world.add_object(server.largepipe, 0)
    for largepipe_bonus in server.largepipes_bonus:
        game_world.add_object(largepipe_bonus, 0)

    for brick in server.bricks:
        game_world.add_object(brick, 0)

    game_world.add_object(server.flag, 0)
    game_world.add_object(server.castle, 0)

    for questionbox_coin in server.questionboxs_coin:
        game_world.add_object(questionbox_coin, 0)
    for questionbox_star in server.questionboxs_star:
        game_world.add_object(questionbox_star, 0)
    for questionbox_supermushroom in server.questionboxs_supermushroom:
        game_world.add_object(questionbox_supermushroom, 0)
    for questionbox_upmushroom in server.questionboxs_upmushroom:
        game_world.add_object(questionbox_upmushroom, 0)
    for questionbox_fireflower in server.questionboxs_fireflower:
        game_world.add_object(questionbox_fireflower, 0)
    # game_world.add_object(propellermushroom, 0)

    for goomba in server.goombas:
        game_world.add_object(goomba, 0)
    game_world.add_object(server.flower, 0)
    game_world.add_object(server.hamerbro, 0)

    game_world.add_object(server.mario, 1)

    server.mario.mario_in_bonusstage = False

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 충돌 체크 및 충돌 처리
    # 마리오 - 땅
    for collision_ground in server.collision_grounds:
        if collision.collide(collision_ground, server.mario):
            left, bottom, right, top = collision_ground.get_bb()
            collide_loc = top + 10

            server.mario.stop(collide_loc)

    # 마리오 - 물음표 상자_코인
    for questionbox_coin in server.questionboxs_coin:
        if collision.collide_all_head(questionbox_coin, server.mario):  # 물음표 상자와 충돌했을 경우
            coin = Coin(120, 0, 30, 30, questionbox_coin.x, questionbox_coin.y)  # 코인 생성
            game_world.add_object(coin, 0)
            server.mario.addCoin()
            server.mario.addScore(200)
            server.questionboxs_coin.remove(questionbox_coin)  # 물음표 상자 충돌 검사하는 리스트에서 제거
            game_world.remove_object(questionbox_coin)  # 충돌한 물음표 상자 삭제
    # 마리오 - 물음표 상자_별
    for questionbox_star in server.questionboxs_star:
        if collision.collide_all_head(questionbox_star, server.mario):  # 물음표 상자와 충돌했을 경우
            star = Star(0, 0, 30, 30, questionbox_star.x, questionbox_star.y)  # 별 생성
            game_world.add_object(star, 0)
            server.mario.addScore(1000)
            server.questionboxs_star.remove(questionbox_star)  # 물음표 상자 충돌 검사하는 리스트에서 제거
            game_world.remove_object(questionbox_star)  # 충돌한 물음표 상자 삭제
    # 마리오 - 물음표 상자_슈퍼버섯
    for questionbox_supermushroom in server.questionboxs_supermushroom:
        if collision.collide_all_head(questionbox_supermushroom, server.mario):  # 물음표 상자와 충돌했을 경우
            supermushroom = SuperMushroom(180, 60, 30, 30, questionbox_supermushroom.x, questionbox_supermushroom.y)  # 슈퍼버섯 생성
            game_world.add_object(supermushroom, 0)
            server.mario.addScore(1000)
            server.mario.changeBigMario()
            server.questionboxs_supermushroom.remove(questionbox_supermushroom)  # 물음표 상자 충돌 검사하는 리스트에서 제거
            game_world.remove_object(questionbox_supermushroom)  # 충돌한 물음표 상자삭제
    # 마리오 - 물음표 상자_업버섯
    for questionbox_upmushroom in server.questionboxs_upmushroom:
        if collision.collide_all_head(questionbox_upmushroom, server.mario):  # 물음표 상자와 충돌했을 경우
            upmushroom = UpMushroom(210, 60, 30, 30, questionbox_upmushroom.x, questionbox_upmushroom.y)  # 업버섯 생성
            game_world.add_object(upmushroom, 0)
            server.mario.addScore(1000)
            server.mario.addLife()
            server.questionboxs_upmushroom.remove(questionbox_upmushroom)  # 물음표 상자 충돌 검사하는 리스트에서 제거
            game_world.remove_object(questionbox_upmushroom)  # 충돌한 물음표 상자삭제
    # 마리오 - 물음표 상자_파이어 플라워
    for questionbox_fireflower in server.questionboxs_fireflower:
        if collision.collide_all_head(questionbox_fireflower, server.mario):  # 물음표 상자와 충돌했을 경우
            fireflower = FireFlower(140, 30, 30, 30, questionbox_fireflower.x, questionbox_fireflower.y)  # 파이어 플라워 생성
            game_world.add_object(fireflower, 0)
            server.mario.addScore(1000)
            server.mario.changeFireMario()
            server.questionboxs_fireflower.remove(questionbox_fireflower)  # 물음표 상자 충돌 검사하는 리스트에서 제거
            game_world.remove_object(questionbox_fireflower)  # 충돌한 물음표 상자삭제

    # 마리오 - 작은파이프
    for smallpipe in server.smallpipes:
        if collision.collide_left_all(smallpipe, server.mario):  # 파이프와 충돌했을 경우
            from MarioBros_Mario import Move_locX
            left, bottom, right, top = smallpipe.get_bb_left()
            collide_loc = left + Move_locX - 10
            server.mario.cantgo_left(collide_loc)  # 앞으로 못 감
        if collision.collide_right_all(smallpipe, server.mario):  # 파이프와 충돌했을 경우
            from MarioBros_Mario import Move_locX
            left, bottom, right, top = smallpipe.get_bb_right()
            collide_loc = right + Move_locX + 11
            server.mario.cantgo_right(collide_loc)  # 앞으로 못 감
        if collision.collide_head_foot(smallpipe, server.mario):  # 위에 올라섰을 경우
            left, bottom, right, top = smallpipe.get_bb_head()
            collide_loc = top + 10
            server.mario.stop(collide_loc)

    # 마리오 - 중간파이프
    if collision.collide_left_all(server.midpipe, server.mario):  # 파이프와 충돌했을 경우
        from MarioBros_Mario import Move_locX
        left, bottom, right, top = server.midpipe.get_bb_left()
        collide_loc = left + Move_locX - 10
        server.mario.cantgo_left(collide_loc)  # 앞으로 못 감
    if collision.collide_right_all(server.midpipe, server.mario):  # 파이프와 충돌했을 경우
        from MarioBros_Mario import Move_locX
        left, bottom, right, top = server.midpipe.get_bb_right()
        collide_loc = right + Move_locX + 11
        server.mario.cantgo_right(collide_loc)  # 앞으로 못 감
    if collision.collide_head_foot(server.midpipe, server.mario):  # 위에 올라섰을 경우
        left, bottom, right, top = server.midpipe.get_bb_head()
        collide_loc = top + 10
        server.mario.stop(collide_loc)

    # 마리오 - 큰파이프
    if collision.collide_left_all(server.largepipe, server.mario):  # 파이프와 충돌했을 경우
        from MarioBros_Mario import Move_locX
        left, bottom, right, top = server.largepipe.get_bb_left()
        collide_loc = left + Move_locX - 10
        server.mario.cantgo_left(collide_loc)  # 앞으로 못 감
    if collision.collide_right_all(server.largepipe, server.mario):  # 파이프와 충돌했을 경우
        from MarioBros_Mario import Move_locX
        left, bottom, right, top = server.largepipe.get_bb_right()
        collide_loc = right + Move_locX + 11
        server.mario.cantgo_right(collide_loc)  # 앞으로 못 감
    if collision.collide_head_foot(server.largepipe, server.mario):  # 위에 올라섰을 경우
        left, bottom, right, top = server.largepipe.get_bb_head()
        collide_loc = top + 10
        server.mario.stop(collide_loc)

    # 마리오 - 보너스맵과 연결된 큰파이프
    for largepipe_bonus in server.largepipes_bonus:
        if collision.collide_left_all(largepipe_bonus, server.mario):  # 파이프와 충돌했을 경우
            from MarioBros_Mario import Move_locX
            left, bottom, right, top = largepipe_bonus.get_bb_left()
            collide_loc = left + Move_locX - 10
            server.mario.cantgo_left(collide_loc)  # 앞으로 못 감
        if collision.collide_right_all(largepipe_bonus, server.mario):  # 파이프와 충돌했을 경우
            from MarioBros_Mario import Move_locX
            left, bottom, right, top = largepipe_bonus.get_bb_right()
            collide_loc = right + Move_locX + 11
            server.mario.cantgo_right(collide_loc)  # 앞으로 못 감
        if collision.collide_head_foot(largepipe_bonus, server.mario):  # 파이프와 충돌했을 때
            server.largepipes_bonus.remove(largepipe_bonus)  # 충돌했을 경우 충돌 검사하는 리스트에서 제거
            game_framework.change_state(MarioBros_BonusStage)  # 보너스맵으로 이동

    # 마리오 - 굼바
    for goomba in server.goombas:
        if collision.collide(goomba, server.mario):  # 굼바와 충돌했을 경우
            server.mario.minusLife()  # 목숨 -1
        elif collision.collide_head_foot(goomba, server.mario):  # 굼바를 밟았을 경우
            goomba.dead()  # 굼바 죽음
            server.goombas.remove(goomba)  # 죽었을 경우 충돌 검사하는 리스트에서 제거
            server.mario.addScore(100)  # 점수 추가

    # 마리오 - 성
    if collision.collide(server.castle, server.mario):  # 성과 충돌했을 경우
        game_framework.change_state(MarioBros_BossStage)  # 보스 스테이지로 이동

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    font = load_font('SuperMario256.ttf', 16)
    numfont = load_font('SuperMario256.ttf', 18)

    from MarioBros_Mario import Mario_score, Mario_life
    font.draw(30, 570, 'MARIO', (255, 255, 255))
    numfont.draw(100, 570, '%06d' % Mario_score, (255, 255, 255))
    numfont.draw(100, 550, 'x', (255, 255, 255))
    numfont.draw(115, 550, '%02d' % Mario_life, (255, 255, 255))

    if server.coin_image == None:
        server.coin_image = load_image('ItemsSheet.png')
    server.coin_image.clip_draw(120, 0, 30, 30, 400, 575)  # 코인 개수 이미지

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
        else:
            server.mario.handle_event(event)
