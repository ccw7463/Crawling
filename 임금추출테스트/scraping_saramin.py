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

url = "https://www.saramin.co.kr/zf_user/salaries/company/enterprise-list"
browser = uc.Chrome(options=options)
browser.get(url)

time.sleep(3)
save_data = {}
isthis_firstpage = True
for _ in range(11):
    for pageidx in tqdm(range(2,12)):
        if isthis_firstpage:
            pageidx -= 1
        for idx in range(1,21):
            category = browser.find_element(By.XPATH,f'//*[@id="salary_list"]/ul/li[{idx}]/div[1]/dl[2]/dd').text
            if not save_data.get(category):
                save_data[category]={}
            company_name = browser.find_element(By.XPATH,f'//*[@id="salary_list"]/ul/li[{idx}]/div[1]/strong/a').text
            avg_salary = browser.find_element(By.XPATH,f'//*[@id="salary_list"]/ul/li[{idx}]/div[2]/span[1]/span/span/span').text
            min_salary = browser.find_element(By.XPATH,f'//*[@id="salary_list"]/ul/li[{idx}]/div[2]/span[2]/span/span/span').text
            max_salary = browser.find_element(By.XPATH,f'//*[@id="salary_list"]/ul/li[{idx}]/div[2]/span[3]/span/span/span').text
            if not save_data[category].get(company_name):
                save_data[category][company_name]={"avg_salary":avg_salary,
                                                "min_salary":min_salary,
                                                "max_salary":max_salary}
            # time.sleep(0.5)
        isthis_firstpage = False
        next_page = browser.find_element(By.XPATH,f'//*[@id="salary_list"]/div[2]/a[{pageidx}]')
        next_page.click()
        time.sleep(2)
    # 저장
    with open("saramin_salary_data.json", "w") as json_file:
        json.dump(save_data, json_file, indent=4)
    # except:
    #     print(f"{_}에서 에러가 발생했습니다.")
    #     print("pageidx :",pageidx)
    #     print("category :",category)
    #     print("company_name :",company_name)
        
    
