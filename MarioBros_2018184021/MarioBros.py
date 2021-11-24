import game_framework
import pico2d

import MarioBros_LogoState
import MarioBros_StartState
import MarioBros_Stage1
import MarioBros_BonusStage
import MarioBros_BossStage

pico2d.open_canvas()
# game_framework.run(MarioBros_LogoState)
game_framework.run(MarioBros_Stage1)
# game_framework.run(MarioBros_BonusStage)
# game_framework.run(MarioBros_BossStage)

pico2d.close_canvas()
