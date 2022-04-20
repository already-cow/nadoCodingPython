#집합 (set) - 중복이 안되고 순서가 없음
my_set = {1, 2, 3, 2, 3}
print(my_set)

java = {"유재석", "하하", "정준하"}
python = set(["유재석", "박명수"]) # list로 정의 후 set으로 감싸기

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 값 추가 및 제외
python.add("하하")
java.remove("유재석")
print(python)
print(java)