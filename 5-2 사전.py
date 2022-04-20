#사전
cabinet = {3:"유재석", 100:"김태호"} # 숫자 아닌 문자도 가능
print(cabinet[3]) # 값이 없으면 오류
print(cabinet.get(100)) # 값이 없으면 None
print(cabinet.get(5,"사용가능")) # 기본값 설정 가능

print(3 in cabinet) # True
print(5 in cabinet) # False

# 새 손님
print(cabinet)
cabinet["a-3"] = "하하"
cabinet[3] = "박명수"
print(cabinet)

# 간 손님
del cabinet["a-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)