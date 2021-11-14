from pico2d import *

class PropellerMushroom:  # 프로펠러 버섯 -> 날기 가능
    image = None

    def __init__(self):
        if PropellerMushroom.image == None:
            PropellerMushroom.image = load_image('ItemsSheet.png')

    def draw(self):
        pass
        #  self.image.clip_draw(0, 80, 30, 30, 250 - Move_locX, 100)