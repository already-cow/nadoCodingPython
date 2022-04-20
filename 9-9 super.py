class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("flyable 생성자")

class flyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()  ---> super는 단일 상속할 때만 사용 가능
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = flyableUnit()