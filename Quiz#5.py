# from random import *

# match = list(range(5, 16))
# unmatch = list(range(16, 51))
# customers = list(range(5, 51))
# shuffle(customers)

# index = 1

# for minute in customers:
#     if minute in match:
#         print("[{2}] {1}번째 손님 (소요시간 : {0}분)".format(minute, index, "O"))
#     elif minute in unmatch:
#         print("[{2}] {1}번째 손님 (소요시간 : {0}분)".format(minute, index, " "))
# # 내가 만든 코드 .. ...


#Answer
from random import *
cnt = 0

for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    elif 15 < time:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {} 분".format(cnt))