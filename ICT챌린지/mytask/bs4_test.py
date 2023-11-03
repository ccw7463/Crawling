
import requests
from bs4 import BeautifulSoup
import pandas as pd
# url = "https://www.google.com/search?q=%EC%8A%A4%EB%A7%88%ED%8A%B8+%EC%86%8C%EB%B0%A9&sxsrf=ALiCzsaVPKU_FES2L7W7nKhUgmxHZ38s1Q:1662425603224&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiDtK78-f75AhUiq1YBHdhsA5oQ_AUoAnoECAIQBA&biw=1680&bih=823&dpr=2"
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, 'lxml')

# result = soup.find_all("div",attrs={"style":"-webkit-line-clamp:3"})
# result = [i.get_text() for i in result]
# print(result)



url = "https://comic.naver.com/webtoon/list?titleId=795658&weekday=tue"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

name = soup.find("span",attrs={"class":"title"}).get_text()
tr = soup.find("tr",attrs={"class":"band_banner v2"})
trs = tr.find_next_siblings()

link_lst = []
num_lst = []
star_lst = []

for i in trs:
    td = i.find("td",attrs={"class":"title"})
    link = "https://comic.naver.com" + td.a["href"]
    link_lst.append(link)
    num = td.a.get_text()
    num_lst.append(num)

    star_td = td.next_sibling.next_sibling
    star = star_td.div.strong.get_text()
    star_lst.append(star)

print(f"웹툰 제목 : {name}")
df = pd.DataFrame({"회차":num_lst,"평점":star_lst,"링크":link_lst})
print(df)
