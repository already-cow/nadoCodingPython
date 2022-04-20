# 마린 : 공격 유닛, 군인, 총
# 탱크 : 공격유닛, 탱크, 일반모드 / 시즈모드
# 레이스 : 공중 유닛, 비행기, 클로킹(상대에게 보이지 않음)
# 메딕 : 의무병
# 파이어뱃 : 공격 유닛, 화염방사기
# 드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송. 공격 불가
# 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사
# 벌쳐 : 지상 유닛, 기동성이 좋음
# 배틀크루저 : 공중 유닛, 체력 높음, 공격력 높음
# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛,

class Unit: # 아래의 함수 소환 위해
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# pass 일단 넘어감
# 건물
class BuildingUnit(Unit): # 어떻게 그냥 넘어가지 ?
    def __init__(self, name, hp, location):
        pass

supply_deport = BuildingUnit("서플라이디폿", 100, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()