class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()  # 100

# 클래스 변수 사용
print(Player.type)  # Player

# 클래스 함수 호출
# Player.where()  # Error
Player.where(player)  # 100 # == player.where() : 객체를 player로 넘겨준 것
