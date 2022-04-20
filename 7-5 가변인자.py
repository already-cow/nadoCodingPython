# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 끝날 때 줄바꿈을 하지않고 이어서 출력
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "python", "java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20,"python", "java", "C", "C++", "C#", "javascript")
profile("김태호", 25, "Kotlin", "Swift")