from random import *
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(lst)
lst = sample(lst,4)

print(
"""-- 당첨자 발표 --
치킨 당첨자 : {}
커피 당첨자 : {}
-- 축하합니다 -- """.format(lst[0], lst[1:]))



#Answer
from random import *
users = list (range(1,21) ) # 1부터 20까지 숫자를 생성
shuffle(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다 -- ")