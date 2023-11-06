from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json
from tqdm import tqdm
import undetected_chromedriver as uc
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
 
# Set up Chrome options
options = uc.ChromeOptions()
# options.add_argument("--headless")
options.add_argument(f"user-agent={my_user_agent}")

url = "https://www.wanted.co.kr/salary/"
browser = uc.Chrome(options=options)
browser.get(url)
time.sleep(3)

# 구글 로그인
login = browser.find_element(By.CLASS_NAME,"Button_Button__interaction__kkYaa")
login.click()
time.sleep(3)

google = browser.find_element(By.CLASS_NAME,"css-15tdtnf")
google.click()
time.sleep(3)

myid = browser.find_element(By.NAME,"identifier")
myid.send_keys("changwoo7463@gmail.com")
time.sleep(3)

okclick = browser.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
okclick.click()
time.sleep(3)

mypw = browser.find_element(By.NAME,"Passwd")
mypw.send_keys("!ckddn960413")
time.sleep(3)

okclick = browser.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button')
okclick.click()
time.sleep(10)

select_element = browser.find_element(By.NAME, "category")
select_element.click()
time.sleep(3)

save_data = {}
for idx in range(2,20):
    large_category = browser.find_element(By.XPATH,f'//*[@id="__next"]/div[3]/div/div[2]/div/div/div[1]/div/select/option[{idx}]')
    if not save_data.get(large_category.text):
        save_data[large_category.text]={}
    print("large_category :",large_category.text)
    large_category.click()
    time.sleep(3)
    for idx2 in tqdm(range(2,44)):
        try:            
            small_category = browser.find_element(By.XPATH,f'//*[@id="__next"]/div[3]/div/div[2]/div/div/div[2]/div/select/option[{idx2}]')
            if not save_data[large_category.text].get(small_category.text):
                save_data[large_category.text][small_category.text]={}
            print("small_category :",small_category.text)
            small_category.click()
            time.sleep(0.5)
            for idx3 in range(2,13):
                year = browser.find_element(By.XPATH,f'//*[@id="__next"]/div[3]/div/div[2]/div/div/div[3]/div/select/option[{idx3}]')
                year.click()
                price = browser.find_element(By.XPATH,f'//*[@id="__next"]/div[3]/div/aside/h2')
                if not save_data[large_category.text][small_category.text].get(year.text):
                    save_data[large_category.text][small_category.text][year.text]=price.text
        except:
            break
    time.sleep(1)

# 딕셔너리를 JSON 파일로 저장
with open("data.json", "w") as json_file:
    json.dump(save_data, json_file, indent=4)
    
# # 직군 분류 선택
# soup = BeautifulSoup(browser.page_source,'lxml')
# option_tags = soup.find_all('option')

# # 가져온 <option> 태그를 순회하면서 내용을 출력하거나 다른 작업을 수행할 수 있습니다.
# for option in option_tags:
#     print(option.text)


# for ii in select_element:
#     print(ii)
# select_element.click()
# print("select_element :",select_element)

# # Select 클래스로 select 요소를 래핑
# select = Select(select_element)

# # 각 option 요소를 선택
# select.select_by_index(0)  # 첫 번째 option 선택
# time.sleep(1)
# select.select_by_index(1)  # 두 번째 option 선택

# find_name = browser.find_element(By.ID,'search.keyword.query')
# find_name.send_keys("37.55218, 127.02083")
# time.sleep(0.3)

# find_button = browser.find_element(By.ID,'search.keyword.submit')
# find_button.send_keys(Keys.ENTER)
# time.sleep(0.3)

# find_gil = browser.find_element(By.CLASS_NAME,'btn_direction')
# find_gil.send_keys(Keys.ENTER)
# time.sleep(0.3)

# start_button = browser.find_element(By.XPATH,'//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[3]/div/div[2]/div[3]/div/div[2]/div/button[1]')
# start_button.send_keys(Keys.ENTER)
# time.sleep(2000)


# login_button = browser.find_element_by_class_name("link_login")
# login_button.click()

# id_button = browser.find_element_by_id("id")
# id_button.send_keys("changwoo7463")

# pw_button = browser.find_element_by_id("pw")
# pw_button.send_keys("!ckddn960413")

# enter_button = browser.find_element_by_class_name("btn_login")
# enter_button(Keys.ENTER)

# browser.find_elements_