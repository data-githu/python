# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:04:13 2020

@author: Owner
"""

■ 35. 이스케이프 문자 이해하기
이스케이프 문자는 키보드로 입력하기 어려운 기호를 나타내기 위해 역슬래쉬 '\' 로 시작 하는 문자입니다.
파이썬에서 자주 사용되는 이스케이프 문자는 다음과 같습니다.
	이스케이프 문자                              설명
		\n                                     줄바꾸기
		\t                                     탭
		\enter                                줄 계속
		\\                                     \기호
		\' 또는 \''                           '기호 또는 ''기호 자체

예제 : 
print('나는 파이썬을 배웁니다. \n 파이썬은 자바보다 \
훨씬 쉽습니다.')


■ 35. 리스트 이해하기 ([ ])
리스트는 파이썬에서 가장 많이 활용되는 시퀀스 자료형 중 하나입니다.
리스트는 [ ] 로 표시하며  [ ] 안에 요소를 콤마(,) 로 구분하여 순서있게 나열합니다.

예제 :
k = ['a','b','c','d','e']
print(k)
print(type(k))

문제122. 동전의 앞면과 뒷면을 포함하는 리스트 코인을 만드시오!
coin = ['앞면', '뒷면']

문제123. 위에서 만든 coin 요소를 10000개로 늘려서 coin_10000 변수에 담으시오!
coin = ['앞면', '뒷면']
coin_10000 = coin*10000
print(coin_10000)

문제124. 위에서 만든 coin_10000리스트에서 표본을 10개를 추출하시오!
import numpy as np

coin = ['앞면', '뒷면']
coin_10000 = coin*10000
print(np.random.choice(coin*10000,10))

설명 : np.random.choice는 numpy 모듈안에 random 코드 안에 choice 함수를 사용하겠다. np.random.choice(모집단 리스트, 샘플 개수)

문제125. 위의 결과에서 앞면이 나오는 횟수를 출력하시오!
import numpy as np
cnt = 0
coin = ['앞면', '뒷면']
coin_10000 = coin*10000

result  = np.random.choice(coin_10000,10)

for i in result:
    if i == '앞면':
        cnt = cnt + 1
print(cnt)

■ 37. 튜플 이해하기 (( ))
튜플은 리스트와 비슷한 성질을 가지고 있는 자료형이지만 요소의 값을 변경할 수 없다는 특징이 있습니다. 리스트는 대괄호 [ ] 로 요소들을 감쌌는데 튜플은 소괄호 ( ) 로 요소를 감쌉니다.
튜플은 데이터가 변경이 안되므로 튜플로 만든 데이터에 대한 신뢰도가 높아집니다.

예제 : 리스트에서 특정 요소를 변경하는 방법
a = [1,2,3,4,5]
print = (type(a))
print(a[0])
a[0] = 7
print(a)

문제126. a리스트에 인덱스번호 3번째 요소를 17로 변경하시오!
a = [7,2,3,4,5]
a[3] = 17
print(a)

예제2: 튜플은 데이터를 변경할 수 없습니다.
b = (1,2,3,4,5)
print(b[0]) #1
b[0] = 7 #ERROR

설명 : 회사에서 변경이 되어서는 안되는 데이터는 프로그래밍 할 때 튜플로 만들어서 관리하면 됩니다.

예를들면 백화점에서 사용하는 포인트 적립카드에서 포인트 적립시 구매금액의 0.01% 로 적립을 해준다고 하면 0.01% 는 절대로 변경되어서는 안되는 데이터 이므로 튜플로 관리합니다.


문제127. 아래의 숫자 데이터들을 튜플로 생성하시오. 튜플의 변수 이름은 point 라고 하세요.
point = (0.01, 0.02, 0.03, 0.04, 0.05)
print(type(point))

문제128. 위의 튜플 point의 요소 중 0.03만 뽑아서 출력하시오!
point = (0.01, 0.02, 0.03, 0.04, 0.05)
print(point[2])

문제129. 위의 튜플의 모든 요소를 다 출력하시오!
point = (0.01, 0.02, 0.03, 0.04, 0.05)
for i in point:
    print(i)

■ 38. 사전 이해하기 ({ })
사전은 키와 값을 하나의 요소로 하는 순서가 없는 집합닙니다.
그러므로 사전은 시퀀스 자료형이 아니며 인덱싱으로 값을 접근할 수 없습니다. 사전은 '키:값' 쌍이 하나의 요소입ㅏ.

예 : 
a={ 'apple' : '사과', 'banana' : '바나나'}
print(a)
print(type(a))
print(a.key( )) #키값들만 출력
print(a.values( )) #값들만 출력
a['grape'] = '포도'

예 : 
b = { } # 비어있는 딕셔너리를 생성합니다.
b['apple'] = '사과'
b['pear'] = '배'
b['grape'] = '포도'

문제130. 아래의 두개의 리스트를 각각 만들고 아래와 같이 fruit 라는 딕셔너리를 생성하시오!
a = ['사과','배','포도','복숭아','바나나']
b=['apple','pear','grape',peach','banana']

결과: print(fruit) # {'사과': 'apple', '배': 'pear', '포도': 'grape', '복숭아': 'peach', '바나나': 'banana'}

a = ['사과','배','포도','복숭아','바나나']
b=['apple','pear','grape','peach','banana']
fruit = { }

for i, k in zip(a,b):
    fruit[i]=k
print(fruit)




