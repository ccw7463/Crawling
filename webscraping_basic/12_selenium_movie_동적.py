# ▷▷▷ 동적 페이지 이용하기 ◁◁◁
'''
동적페이지 : 사용자가 동작했을때 변하는 페이지
    - 스크롤 내리면 새로운 창 계속해서 나타나는거
    - selenium 을 통해 구현
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1. 페이지 이동
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"

browser = webdriver.Chrome()
browser.get(url)

# 2. 스크롤 내리기 
'''
browser.execute_script("window.scrollTo(0,내릴크기)")
    - 1. 적힌 숫자만큼 스크롤 내리기
    - 2. document.body.scrollHeight : 창 화면크기 만큼 
'''

# 3. 끝까지 스크롤 계속 내리기

interval = 2 
prev_height = browser.execute_script("return document.body.scrollHeight") # 현재 문서 높이를 저장

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 화면높이만큼
    time.sleep(interval)
    current_height = browser.execute_script("return document.body.scrollHeight") # 현재 문서 높이를 저장

    if current_height == prev_height:
        print("--------- 스크롤이 끝났습니다 ---------")
        break
    else:
        prev_height = current_height
    

# ▷▷▷ 스크래핑 작업 수행 ◁◁◁
'''
selenium 을 통해서 페이지를 열었기때문에
selenium 을 통해서 페이지소스를 가져올 수 있다.
    - 따라서 url과 headers 정보는 필요없음
    기존 : soup = BeautifulSoup(res.text,"lxml")
    변경 : soup = BeautifulSoup(browser.page_source,"lxml")
        - 페이지에서 HTML 정보 로드시 --> page_source
'''
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source,"lxml")
names = soup.find_all("div",attrs={"class":"WsMG1c nnK0zc"})

count=0
for name in names:
    print(name.get_text())
    count = count+1
print(count)

with open("movie.html",'w',encoding='utf8') as f:
    # f.write(res.text)
    f.write(soup.prettify()) # html 문서를 예쁘게 출력


print("--------------time sleep--------------")
time.sleep(5)


