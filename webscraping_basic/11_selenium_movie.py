'''
접속하는 사용자의 헤더정보를 통해서 그에 맞는 웹페이지 보여줌
    - 한글로 잘 보여주는 웹페이지를 얻어내려면 user agent 사용
    - 'Accept-Language":"ko-KR,ko" 를 사용해서 한글전용 페이지를 얻어냄
'''

from email import header
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
           "Accept-Language":"ko-KR,ko"
           }

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
names = soup.find_all("div",attrs={"class":"WsMG1c nnK0zc"})

count=0
for name in names:
    print(name.get_text())
    count = count+1
print(count)

with open("movie.html",'w',encoding='utf8') as f:
    # f.write(res.text)
    f.write(soup.prettify()) # html 문서를 예쁘게 출력



