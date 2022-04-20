site = "http://google.com"
my_site = site.replace("http://", "")
# print(my_site)
my_site = my_site[:my_site.index(".")]
# print(my_site)

print("생성된 비밀번호 : {}{}{}{}".format(my_site[0:3],len(my_site),my_site.count("e"),"!"))



#Answer
url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1} 입니다.".format(url, password))