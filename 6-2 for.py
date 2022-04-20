#for (반복문)
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))

customers = ["토르", "아이언맨", "그루트"]
for starbucks in customers:
    print("{0}님 커피가 준비되었습니다.".format(starbucks))