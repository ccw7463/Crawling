# 코스피 시가총액 순위 1~200 스크래핑

import requests
import re
from bs4 import BeautifulSoup
from scipy.misc import face

print("@@@시작@@@")

lst1=[]
lst2=[]
lst3=[]
lst4=[]
lst5=[]
lst6=[]
lst7=[]

for page in range(1,5):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(str(page))
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    kospi = soup.find_all("td",attrs={"class":"no"})
    for i in range(0,50):
        kospi_type = kospi[i].find_next_siblings("td")
        name = kospi_type[0].get_text()
        present_price = kospi_type[1].get_text()
        plus_minus = kospi_type[2].get_text().strip()
        fluc_rate = kospi_type[3].get_text().strip()
        face_value = kospi_type[4].get_text()
        market_cap = kospi_type[5].get_text()
        trading_volume = kospi_type[8].get_text()

        lst1.append(name)
        lst2.append(present_price)
        lst3.append(plus_minus)
        lst4.append(fluc_rate)
        lst5.append(face_value)
        lst6.append(market_cap)
        lst7.append(trading_volume)


import pandas as pd
df = pd.DataFrame({"name":lst1,"present_price":lst2,"plus_minus":lst3,"fluc_rate":lst4,"face_value":lst5,"market_cap":lst6,"trading_volume":lst7})
print(df)

df.to_csv("kospi.csv")

