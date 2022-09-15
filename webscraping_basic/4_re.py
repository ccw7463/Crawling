# ▷▷▷ 정규식 라이브러리 사용 ◁◁◁
import re

'''
. (ca.e) : 하나의 문자를 의미 --> care, cafe, case 
^ (^de) : 문자열의 시작 --> desk, destination
$ (se$) : 문자열의 끝 --> case, base
'''

# ▷▷▷ re.compile 을 통해 패턴을 받아옴 ◁◁◁ 
p = re.compile("ca.e") 

# ▷▷▷ 패턴을 매치하기 ( 매칭이 안맞을경우 에러발생 ) ◁◁◁
# 메소드1. match 메소드 : 주어진 문자열의 처음부터 일치하는지 확인
m1 = p.match("careless")

def match_test(m):
    if m:
        print(m.group()) # --> 일치하는 문자열 반환
        print(m.string) # --> 입력받은 문자열 (여기서 m)
        print(m.start()) # --> 일치하는 문자열의 시작 인덱스
        print(m.end()) # --> 일치하는 문자열의 끝 인덱스
        print(m.span()) # --> 일치하는 문자열의 시작 / 끝 인덱스
    else:
        print("매칭되지 않음")

match_result = match_test(m1)
print(match_result,"\n")

# 메소드2. search 메소드 : 주어진 문자열 중에 일치하는게 있는지 확인
m2 = p.search("good care")

match_result = match_test(m2)
print(match_result,"\n")

# 메소드3. findall 메소드 : 일치하는 모든것을 리스트 형태로 반환
lst = p.findall("good care cafe cave")
print(lst)