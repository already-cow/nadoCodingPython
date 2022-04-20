print("Python", "Java", sep=",") # 사이사이에 어떤 것을 넣을지 결정

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요 ?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성정
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(5), str(score).rjust(3), sep=":")

# 은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요.")
print("입력하신 값은" + answer + "입니다.")

# answer = 10 값을 입력하면 type은 int
# answer = input의 type은 str
