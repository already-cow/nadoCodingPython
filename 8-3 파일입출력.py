score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 50", file = score_file)
print("영어 : 100", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
print("과학 : 50", file = score_file)
print("코딩 : 100", file = score_file)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 리스트로 저장
for line in lines:
    print(line, end="")
score_file.close()

# for은 리스트를 하나씩 나타내주는 함수