import requests
from bs4 import BeautifulSoup

# webtoon 메인 페이지 제목 전부 들고오기
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("a",attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())


# 퀘스트 지상주의 정보(제목,링크,평점) 가져오기
url = "https://comic.naver.com/webtoon/list?titleId=783052&weekday=mon"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("td",attrs={"class":"title"})
stars = soup.find_all("div",attrs={"class":"rating_type"})

for cartoon,star in zip(cartoons,stars):
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    grade = star.strong.get_text()
    print(title, link, grade)
