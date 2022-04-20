# 프로그램 상에서 사용하는 데이터를 파일형태로
# pickle을 쓰기위해선 b(바이너리), 인코딩 불필요

import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":40, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile의 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file의 정보를 profile에 불러오기
print(profile)
profile_file.close()
