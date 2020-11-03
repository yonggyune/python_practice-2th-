number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

print(number ,'번 손님', greeting, '.', place, '에 오신 것을',welcome, '!')

base = '{}번 손님, {}.{}에 오신것을 {}!'
new_way = base.format(number, greeting, place, welcome)

print(base)
print(new_way)

mine = '가위'
yours = '바위'
result = '졌다..'

print('나는 {}, 너는 {}, 그래서 {}'.format(mine, yours,result))
## 괄호의 수가 맞지않으면 안나올 수가 있고 오류가 나올 수도 있따
# 괄호의수가 더 많으면 에러 발생 괄호의 수가 적으면 괄호의 수가까지 받고 에러가 발생하지는 않음

##################################### 문자열 (quote) ####################

string1 = 'some text'
string2 = '어떤 텍스트'
string3 = '{}도 {}도 지금 이것도 문자열'.format(string1,string2)

print(string1,string2, string3)

quote = '문법검사가 왈 "직접인용은 큰 따옴표이다!"'
emphasize = "'문법검사기'를 인용하다니"
error = "엄마 친구 아들이 파이썬이 좋아라고 했대"
### 큰따옴표 안에 큰타옴표를 사용하면 파이썬이 문장의 중간에서 string을 끝내버림

### 파이썬의 경우 따옴표는 같은 줄에서 끝내기를 기대하는 편 따라서 따옴표 세개를 사용하면 줄을 바꿔도 같은 문자열로 인식
## 단 같은 종류의 따옴표를 사용할 것
