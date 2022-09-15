# ▷▷▷ 두개의 라이브러리 import ◁◁◁
# 1. beautifulsoup : 스크래핑 하기위해서 사용되는 라이브러리
# 2. lxml : 구문을 분석하는 parser

import requests
from bs4 import BeautifulSoup

# ▷▷▷ 기본 틀 ◁◁◁
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml") 

'''

1.url 정의 : url = "http://~~~"
2.정보담을 객체정의 : res = requests.get(url)
3.오류검사 : res.raise_for_status()
4.bs4 객체정의 : soup = BeautifulSoup(res.text,"lxml")
    - html 문서정보인 res.text를 lxml 파서를 통해 객체지정
    - 해당 객체를 통해 html 정보의 elemnet 들에 접근 가능

'''

# ▷▷▷ 기본 메소드 정리 ◁◁◁
'''

@ : beautifulsoup 객체
$ : element

@.a : 첫번째로 발견되는 a tag가 있는 element를 리턴
@.a.attrs : a tag가 있는 element의 속성값들을 딕셔너리 형태로 리턴
@.$.get_text() : 문장만 뽑아내기
@.find("원하는 tag","조건") : 조건에 알맞는 원하는 tag의 element 리턴
                    - 조건 형태
                        1. attrs = {element 명 : 내용}
                        2. text = "ㅇㅇㅇ"
                    - attrs 라는게, element의 속성값을 딕셔너리로 뽑는것
                    - 따라서 원하는 tag인 element를 찾을건데, 조건이 속성값이 ~인 애다
@.find_all("원하는 tag","조건") : 조건에 알맞는 원하는 tag의 element 전부 리스트로 가져옴

'''
soup.a
soup.a.attrs
soup.title.get_text()

soup.find("a",attrs={"class":"Nbtn_upload"}) # "class가 Nbtn_upload인 a element를 찾아줘"
                                             # a tag인 element인데, 속성값이 class=Nbtn_upload인 애를 찾아줘
soup.find(attrs={"class":"Nbtn_upload"}) # "class가 Nbtn_upload인 어떤 element 찾아줘"


# ▷▷▷ 형제, 부모 메소드 ◁◁◁
'''

@.find 결과를 다시 객체로 받을 수 있음. 
  - 그래서 @.find 결과에서 원하는 태그값만 얻을 수 있음.
  - rank1 = soup.find("li",attrs={"class":"rank01"})

1. rank1.next_sibling.next_sibling : 다음 형제 element로 넘어가기
    - 두번 해주는이유는 사이에 개행이 있기때문 (한번 해주면 결과안나옴)
    - 주로 사용 : rank1.find_next_sibling("li") → 개행상관X

2. rank2.previous_sibling.previous_sibling : 이전 형제 element로 넘어가기
    - 두번 해주는이유는 사이에 개행이 있기때문 (한번 해주면 결과안나옴)
    - 주로 사용 : rank1.find_previous_sibling("li") → 개행상관X

3. rank1.parent : 부모 태그로 넘어가기

4. 한번에 찾기
    - rank1.find_next_siblings("li") : li 태그를 가진 형제들을 모두 가져옴
'''

rank1 = soup.find("li",attrs={"class":"rank01"}) 
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
rank4 = rank3.next_sibling.next_sibling
print(rank1.a.get_text())
print(rank2.a.get_text())
print(rank3.a.get_text())
print(rank4.a.get_text())