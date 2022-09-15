'''
웹 애플리케이션 테스트를 위한 포터블 프레임워크
    - 웹페이지 자동화 가능
설치 필요 요소
1. selenium 설치
    - pip install selenium
2. 웹 드라이버 (크롬용 다운로드)
    - 버전 정보확인
        - chrome://version/
        - 설정 >> chrome 정보
        - 내 크롬 버전 : 98.0.4758.102 
    - chrome driver 다운로드 
        - 검색 : chromedriver
        - 버전에 맞는것 다운로드
        - 내 작업 폴더내에 압축풀기
3. 해당 chromedriver 로 크롬을 제어
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ▷▷▷ 기본 틀 ◁◁◁
'''
beautifulsoup 에서는 requests 객체 정의 --> beautifulsoup 객체 정의 진행
selenium 에서는 browser 객체 정의만 진행
'''
dir = "C:/Users/infosec/WORKSPACE/inflearn/crawling0221/crawling/chromedriver.exe"
url = "http://naver.com"
browser = webdriver.Chrome(dir) # 실행 파일과 chromedriver가 같은 경로일경우 Chrome() 만 해도 됨
browser.get("http://naver.com")

# ▷▷▷ 메소드 정리 ◁◁◁
'''
@ : element
1. 탐색
    - @.find_element_by_변수명
    - 클래스 : @.find_element_by_class_name
    - id : @.find_element_by_id
    - tag : @.find_element_by_tag_name
        - 복수개를 들고올경우 element --> elements
    - xpath : @.find_element_by_xpath("경로")
        - F12 --> 원하는 element "copy xpath" 수행 --> 경로부분에 마우스우클릭 수행
    - 속성값 얻기 : @.get_attribute("href")
        - 예) 1. elem = browser.find_element_by_tag_name("a")
              2. for e in elem:
                    e.get_attribute("href")
            --> "a" 태그를 가지는 모든 element의 링크를 가져옴
2. browser 메소드
    - browser.back() : 뒤로 가기
    - browser.forward() : 앞으로 가기
    - browser.refresh() : 새로고침
    - browser.close() : 현재 탭 끄기
    - browser.quit() : 브라우저 전체 끄기
3. 객체.click() : 클릭
    - @.click()
4. 글/명령어 보내기
    - @.send_keys("창우")
    - @.send_keys(Keys.ENTER)
'''
# 네이버로그인 클릭
login_main = browser.find_element_by_class_name("link_login")
login_main.click()

# 아이디 / 비번 입력
id_input = "changwoo7463"
pw_input = "!ckddn960413"
login_sub = browser.find_element_by_class_name("btn_login")

id = browser.find_element_by_id("id")
id.send_keys(id_input)

pw = browser.find_element_by_id("pw")
pw.send_keys(pw_input)

login_sub.click()

# 오류 발생후 새로운 아이디 입력
'''
1. 실행간에 시간차 gap을 두기 위해 time.sleep 사용
2. 이미 작성되어 있는 id 를 지우기 위해 elem.clear() 사용
'''
import time
time.sleep(3)

id = browser.find_element_by_id("id")
id.clear()
id.send_keys("dddd")


# HTML 정보 출력
'''
현재 열려있는 페이지의 HTML 정보를 파싱하기위한 방법
    - @.page_source
'''
print(browser.page_source)
browser.quit()