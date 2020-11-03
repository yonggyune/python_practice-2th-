"""for {1} in {2}
1 이라는 변수에 {2}의 값들을 하나씩 대입하고 실행한다는 의미 
{1} = {2}[0]
{1} = {2}[1]
......
이런 느낌 
"""


"""
for i in range():
range에 5를 넣으면 5개의 숫자를 사용가능 but 0 부터 시작함 !!! 
"""

names = ['철수', '영희' ,'바둑이','귀도','비단범']

for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i+1 , name))

for i, name in enumerate(names):
    print('{}번: {}'.format(i+1, name))

"""
enumerate ???? 두개의 변수를 모두 받는 for 반복문을 사용 가능 순서와 list 값을 가져 간다 
"""