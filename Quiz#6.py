def std_weight(height, gender):
    if gender == "여자":
        weight = round(height * height * 0.0021, 2)
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
    elif gender == "남자":
        weight = round(height * height * 0.0022, 2)
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
    else:
        print("성별을 다시 입력해주십시오.")

std_weight(163, "여자")


#Answer
def std(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
