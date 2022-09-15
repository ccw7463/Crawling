# 이미지 다운받기
'''
requests 에서 가져온 정보에서 이미지저장시 .content 사용
'''
import requests
from bs4 import BeautifulSoup
import re


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
number = 0 # 사진 이름 번호
for year in range(2015,2022):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.text,"lxml")
    images = soup.find_all("img",attrs={"class":"thumb_img"})

    # image url 지정
    for idx,image in enumerate(images):
        image_url = image["src"]

        if image_url.startswith("//"):
            image_url = "https:" + image_url
        print(image_url)

        # 이미지 url에서 정보 가져옴
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # 이미지 저장 (이미지는 텍스트가 아니므로 wb 사용)
        with open("movie{}.jpg".format(number+1),'wb') as f:
            f.write(image_res.content)
        
        # 사진 이름 번호 증가
        number = number + 1
        
        # 상위 5개 이미지만 다운 받겠음.
        if idx >= 4:
            break

    print("-"*100)