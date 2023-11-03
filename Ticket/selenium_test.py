from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
url = "https://www.naver.com/"
url = "https://map.kakao.com/link/to/화재발생현장, 37.54818, 127.02083"
dir = "C:/Users/chang/Desktop/개인공부/Crawling/mytask/chromedriver.exe"
browser = webdriver.Chrome(dir)
browser.get(url)

find_name = browser.find_element(By.ID,'search.keyword.query')
find_name.send_keys("37.55218, 127.02083")
time.sleep(0.3)

find_button = browser.find_element(By.ID,'search.keyword.submit')
find_button.send_keys(Keys.ENTER)
time.sleep(0.3)

find_gil = browser.find_element(By.CLASS_NAME,'btn_direction')
find_gil.send_keys(Keys.ENTER)
time.sleep(0.3)

start_button = browser.find_element(By.XPATH,'//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[3]/div/div[2]/div[3]/div/div[2]/div/button[1]')
start_button.send_keys(Keys.ENTER)
time.sleep(2000)


# login_button = browser.find_element_by_class_name("link_login")
# login_button.click()

# id_button = browser.find_element_by_id("id")
# id_button.send_keys("changwoo7463")

# pw_button = browser.find_element_by_id("pw")
# pw_button.send_keys("!ckddn960413")

# enter_button = browser.find_element_by_class_name("btn_login")
# enter_button(Keys.ENTER)

# browser.find_elements_