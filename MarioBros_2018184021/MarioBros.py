import game_framework
import pico2d

import MarioBros_LogoState
import MarioBros_StartState
import MarioBros_Stage1

pico2d.open_canvas()
# game_framework.run(MarioBros_LogoState)
game_framework.run(MarioBros_Stage1)
pico2d.close_canvas()
