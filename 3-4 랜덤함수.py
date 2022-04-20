#랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만 임의의 값 생성
print(int(random() * 100)) # 0 ~ 100 미만 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하 임의의 값 생성