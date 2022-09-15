# ▷▷▷ requests 라이브러리 사용 ◁◁◁
import requests

# ▷▷▷ requests.get(URL) : 해당 URL에 접속하여 정보를 가져옴 ◁◁◁
res = requests.get("http://google.com") 

# ▷▷▷ 해당 URL에 대해 문제가 없는지 확인 : 200(requests.codes.ok)이면 정상 ◁◁◁
print("응답코드 :", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 발생하였습니다.")

# ▷▷▷ 문제가 발생하면 자동 종료하기 : 얘 한문장이면 위 과정 생략가능해짐 ◁◁◁
res.raise_for_status()


# ▷▷▷ 결과보기 (res.text : 해당 url의 html 문서를 가져옴) ◁◁◁
print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)


'''
requests 를 통해 "http://nadocoding.tistory.com"을 들어갈 때 에러발생
그 이유는 부적절한 경로로 접근할 시 보안상으로 차단하기 때문
해당 문제를 해결하기 위한 방법이 user_agent

검색창에서 user agent string 검색해서 해당 홈페이지를 들어가면
내 컴퓨터/휴대폰의 user agent 정보를 얻을 수 있음.
물론 접속하는 브라우저 (크롬,엣지등) 에 따라 상이함
'''

import requests

headers = {"Users-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

res = requests.get("http://nadocoding.tistory.com",headers=headers)

res.raise_for_status()

with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)

