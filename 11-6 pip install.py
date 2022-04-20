# pypi.org 필요한 패키지 사용

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# package 설치법
# 터미널에 pip list 하면 현재 설치되어있는 packge 정보
# 터미널에 pip show beautifulsoup4 하면 정보
# 터미널에 pip install -- upgrade beautifulsout4 하면 업그레이드 가능
# 터미널에 pip uninstall beautifulsoup4 하면 삭제