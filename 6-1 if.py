#IF
weather = input("오늘 날씨는 어때요 ?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("오늘 기온은 어때요 ?")) # input -> str을 받아서 int 변환
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 20 <= temp and temp <30:
    print("조금 덥지만 괜찮은 날씨에요")
elif 10 <= temp < 20:
    print("겉옷을 챙겨 산책하기 좋은 날씨에요")
elif temp <10:
    print("동상위험")