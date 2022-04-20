def profile(name, age, main_lang):
    print("이름 : {0}\t나이 :{1}\t주 사용 언어 :{2}" \
        .format(name, age, main_lang))

profile("유재석", 20, "python")
profile("김태호", 25, "java")

def prof(name, age=17, main_lang="python"):
    print("이름 : {0}\t나이 :{1}\t주 사용 언어 :{2}" \
        .format(name, age, main_lang))

prof("유재석")
prof("김태호")
prof("박명수")