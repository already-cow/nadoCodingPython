# while 조건을 만족할 때까지 반복

customers = "토르"
index = 5
while index >=1: # <- 조건
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customers, index))
    index -= 1
    if index == 0:
        print("커피가 폐기되었습니다.")

# index = 0
# while True:
# index += 1 무한루프에 빠지면 ctrl+c를 이용해 멈춤

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요 ?")