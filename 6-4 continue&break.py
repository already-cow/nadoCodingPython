#continue & break

absent = [2, 5] # 결석
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue # 뛰어넘고 출력
    print("{0}, 책을 읽어봐".format(student))


absent = [3, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("end. come {0}".format(no_book))
        break
    print("{0}, read a book".format(student))