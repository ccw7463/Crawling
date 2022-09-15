'''
셀레니움을 통해 웹스크래핑을 하다보면 
매번 브라우저를 띄우면서 진행되기 떄문에 속도가 느리다.
    - 화면을 볼 필요가 없고, 서버피시에서 진행을 한다면은
      굳이 창을 띄우거나 할 필요 없음
    - 이때 사용하는 기능이 "Headless"
'''

from selenium import webdriver
import time

# headless 로 실행하기 (options 설정)
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2496x1664") # 실제 띄우진 않지만 브라우저의 창 크기를 명시해줄수있음 
browser = webdriver.Chrome(options=options)


# 테스트 해보기
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"
browser.get(url)

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
    

# 실행되고 있는 브라우저의 현재화면 캡처
browser.get_screenshot_as_file("google_movie.png")