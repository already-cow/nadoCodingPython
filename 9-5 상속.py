# 마린 : 공격 유닛, 군인, 총
# 탱크 : 공격유닛, 탱크, 일반모드 / 시즈모드
# 레이스 : 공중 유닛, 비행기, 클로킹(상대에게 보이지 않음)
# 메딕 : 의무병
# 파이어뱃 : 공격 유닛, 화염방사기

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        

# 공격 유닛
class AttackUnit(Unit): # 상속 받을 유닛을 정함
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속 받을 init
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
