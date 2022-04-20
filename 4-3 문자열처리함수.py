#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 0번째 문자가 대문자니 ?
print(len(python)) # 문자 길이
print(python.replace("Python", "Java")) # 문자 바꾸기

index = python.index("n") # 첫번째 n위치
print(index)
index = python.index("n", index + 1) # 두번째 n위치
print(index)

print(python.find("n"))
print(python.find("Java"))
# find는 없으면 -1
# index는 없으면 오류

print(python.count("n")) # 문자 세기