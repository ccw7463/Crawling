from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.naver.com/"
browser = webdriver.Chrome("chromedriver")
browser.get(url)

login_button = browser.find_element_by_class_name("link_login")
login_button.click()

id_button = browser.find_element_by_id("id")
id_button.send_keys("changwoo7463")

pw_button = browser.find_element_by_id("pw")
pw_button.send_keys("!ckddn960413")

enter_button = browser.find_element_by_class_name("btn_login")
enter_button(Keys.ENTER)

browser.find_elements_