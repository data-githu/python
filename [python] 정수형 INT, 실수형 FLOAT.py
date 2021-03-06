# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:13:41 2020

@author: Owner
"""


■ 69. 실수형 자료를 정수형 자료로 변환하기 (int)
*파이썬 변환함수 정리
                 데이터 유형               변환함수
정수형          int                          int(emp)
문자형          str                           str()
실수형          float                        float()
리스트형       list                           list()
튜플형          tuple                       tuple()

코드 작성시 수학연산을 하다보면 정수끼리만 계산해야하는 경우가 있습니다. 이때 우리가 가진 데이터가 실수형이라면 실수형 자료를 정수형으로 변환한 후에 계산을 해주어야 합니다.
파이썬 내장함수 int() 는 인자로 입력된 실수형 자료를 정수형 자료로 변화해줍니다.
int()는 입력된 실수형 자료의 소수부분은 버리고 정수부분만 취하여 정수값으로 리턴합니다.

예 : print(int(-5.4)) #-5

문제234. 판다스를 이용해서 emp3.csv를 읽어서 이름과 월급을 출력하는데 월급을 출력할때 소수점 이하는 버리고 정수부분만 출력되게하세요.
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename', 'sal']])

설명 : int() 함수를 따로 쓰지 않아도 정수형으로 출력되고 있습니다.
판다스를 이용하지 않았을 때와 다르게 숫자는 바로 숫자형으로 출력해주고 있습니다.



■ 70. 정수형 자료를 실수형 자료로 변환하기 (float)
이미지 처리나 공학용 프로그램을 작성할 때 실수형 끼리만 계산해야하는 경우가 많습니다. 이때 우리가 가진 데이터가 정수형이라고 하면 정수형 자료를 실수형 자료로 변환한 후에 계산해주어야 합니다. 파이썬 내장함수 float() 은 인자로 입력된 정수형 자료를 실수형으로 변환해줍니다.

예제 : print(float(10)) #10.0

문제235. 판다스를 이용해서 이름과 월급을 출력하는데 월급을 출력할때 실수형으로 출력하시오!
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
emp['sal'] = emp['sal'].apply(float)  #emp 데이터프레임의 sal 컬럼의 데이터를 float로 변환해서 emp 데이터프레임에 sal 컬럼의 데이터로 변경해라.
print(emp['sal'])
print(emp[['ename','sal']])

