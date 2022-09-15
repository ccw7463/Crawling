from curses import beep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

text1 = "AI"
text2 = "화재"
url = f"https://www.google.com/search?q={text1}+{text2}&tbm=nws"

# 셀레니움
browser = webdriver.Chrome("chromedriver")
browser.get(url)

# bs4
res = requests.get(url)
soup = BeautifulSoup(browser.page_source,'lxml')

# 같이 사용하기
all_result = []
for i in range(1,100):
    try:
        soup = BeautifulSoup(browser.page_source,'lxml')
        result = list(map(lambda x:x.get_text(),soup.find_all("div",attrs={"role":"heading"})))
        all_result.extend(result)
        time.sleep(1)
        next_page = browser.find_element_by_xpath('//*[@id="pnnext"]/span[2]') # 풀패스말고 그냥 xpath하니까 에러없이 잘되는듯?
        next_page.click()
        time.sleep(1.5)
    except:
        print("마지막페이지 입니다.")
        break

print("===== 크롤링 끝 =====")
import pandas as pd
df = pd.DataFrame({"crawling":all_result})
df.to_csv("result.csv",encoding="utf-8-sig")