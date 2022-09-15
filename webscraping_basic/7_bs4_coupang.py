import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

# 1~5 페이지에 대해서 수행
for page in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(page)
    print("◈◈ {} 페이지입니다.◈◈".format(page))
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    # 정규식을 이용한 find
    items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
    count = 0

    for i in items:

        # 추가 할인 쿠폰 상품 제외
        # --> 문자열끝에 공백한칸있었네 어쩐지안되더라
        coupon = i.find("span",attrs={"class":"badge badge-benefit "})
        if coupon:
            print("   <<추가 할인 쿠폰 상품 제외합니다.>>")
            continue
        else:
            pass
        
        # 상품 개수
        count = count + 1

        # 변수
        link = "https://www.coupang.com"+i.a["href"]
        name = i.find("div",attrs={"class":"name"}).get_text()
        rate = i.find("em",attrs={"class":"rating"})
        ori_price = i.find("del",attrs={"class":"base-price"})
        dis_per = i.find("span",attrs={"class":"instant-discount-rate"})
        dis_price = i.find("strong",attrs={"class":"price-value"})
        if (rate and ori_price and dis_per and dis_price):
            rate = rate.get_text()
            ori_price = ori_price.get_text()
            dis_per = dis_per.get_text()
            dis_price = dis_price.get_text()
        else:
            rate = "평점 없음"
            ori_price = "기본 가격 없음"
            dis_per = "할인 퍼센트 없음"
            dis_price = "할인된 가격 없음"
        
        # 출력하기
        if rate=="5.0":
            print(f"제품명 : {name}")
            print(f"평점 : {rate}")
            print(f"기본가격 :{ori_price}")
            print("할인%".format(dis_per))
            print(f"할인된 가격:{dis_price}")
            print(f"link :{link}")
            print("-"*100)
        else:
            continue
        
    
    
    print(count)