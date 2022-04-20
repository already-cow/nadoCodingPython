# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104
student = [1, 2, 3, 4, 5]
student = [i+100 for i in student]
print(student)

student = ["Ashitaka", "Totoro", "Haku"]
student = [len(i) for i in student]
print(student)

student = ["Ashitaka", "Totoro", "Haku"]
student = [i.upper() for i in student]
print(student)