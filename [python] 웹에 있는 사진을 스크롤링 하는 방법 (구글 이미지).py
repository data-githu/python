# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:23:49 2021

@author: Owner
"""

■  146. 웹에 있는 사진을 스크롤링 하는 방법 (구글 이미지)

 딥러닝 기술 ?  1. cnn : 인공지능의 눈
                        예: 관련된 학습 빅데이터 ?  이미지 

                    2. rnn :  인공지능의 입과 귀
                         예: 관련된 학습 빅데이터 ?  자연어 처리를 위한 문장들

 셀레니움을 써서 마치 손으로 클릭해서 이미지를 저장하듯이 저장을 하는데 컴퓨터를 시켜서 자동화 시키는 방법으로 스크롤링을 합니다.

 < 구글에서 이미지 스크롤링 하기  >

1.  크롬 웹브라우져가 설치 되어져 있어야 합니다.

2.  c 드라이브 밑에 chromedriver 폴더를 생성하고 거기에 
    chromedriver.exe 를 넣어야 합니다. 

3.  c 드라이브 밑에 gimages 폴더를 생성합니다.

4.  다운받을 이미지 키워드를 결정합니다.  햄버거 

5.  아나콘다 프롬프트 창을 열고 selenium 을 설치합니다.

  conda  install  selenium 

  conda  list  selenium  

  또는 

  pip  install  selenium 

6. 구글에서 햄버거로 검색했을때 웹스크롤링 코드 

######################################################

import urllib.request # 웹 url을 파이썬이 인식 할 수 있게하는 패키지
from  bs4 import BeautifulSoup # html에서 데이터 검색을 용이하게 하는 패키지
from selenium import webdriver  
# selenium : 웹 애플리케이션의 테스트를 자동화하기 위한 프레임 워크 
# 손으로 클릭하는것을  컴퓨터가 대신하면서 스크롤링하게 하는 패키지

from selenium.webdriver.common.keys import Keys
import time       # 중간중간 sleep 을 걸어야 해서 time 모듈 import

########################### url 받아오기 ###########################

# 웹브라우져로 크롬을 사용할거라서 크롬 드라이버를 다운받아 아래 파일경로의 위치에 둔다
# 팬텀 js로 하면 백그라운드로 실행할 수 있음
binary = 'C:\chromedriver/chromedriver.exe'

# 브라우져를 인스턴스화
browser = webdriver.Chrome(binary)

# 구글의 이미지 검색 url 받아옴(아무것도 안 쳤을때의 url) 
browser.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ei=l1AdWbegOcra8QXvtr-4Cw&ved=0EKouCBUoAQ") 

# 구글의 이미지 검색에 해당하는 input 창의 id 가 '  ?  ' 임(검색창에 해당하는 html코드를 찾아서 elem 사용하도록 설정)
# input창 찾는 방법은 원노트에 있음

# elem = browser.find_elements_by_class_name('gLFyf gsfi') # Tip : f12누른후 커서를 검색창에 올려두고 id를 찾으면 best

elem = browser.find_element_by_xpath("//*[@class='gLFyf gsfi']")  # 위의 코드대로 하거나 이렇게 하거나 둘 중 하나 select


########################### 검색어 입력 ###########################

# elem 이 input 창과 연결되어 스스로 햄버거를 검색
elem.send_keys("햄버거") # 여기에 스크롤링하고싶은 검색어를 입력

# 웹에서의 submit 은 엔터의 역할을 함
elem.submit()

# 현재 결과 더보기는 구현 되어있지 않은상태 -> 구글의 경우 400개 image가 저장됨.

########################### 반복할 횟수 ###########################

# 스크롤을 내리려면 브라우져 이미지 검색결과 부분(바디부분)에 마우스 클릭 한번 하고 End키를 눌러야함

for i in range(1, 6): # 5번 스크롤 내려가게 구현된 상태 range(1,5)
    browser.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(10)          # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌 / 키보드 end키를 총 5번 누르는데 end1번누르고 10초 쉼

time.sleep(10)                      # 네트워크 느릴까봐 안정성 위해 sleep 해줌(이거 안하면 하얀색 이미지가 다운받아질 수 있음.)
html = browser.page_source         # 크롬브라우져에서 현재 불러온 소스 가져옴
soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정


browser.find_element_by_xpath("//*[@class='mye4qd']").click()  # 여기가 결과 더보기 코드입니다

for i in range(1, 5): # 4번 스크롤 내려가게 구현된 상태 range(1,5)
    browser.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(10)          # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌 / 키보드 end키를 총 5번 누르는데 end1번누르고 10초 쉼

time.sleep(10)                      # 네트워크 느릴까봐 안정성 위해 sleep 해줌(이거 안하면 하얀색 이미지가 다운받아질 수 있음.)
html = browser.page_source         # 크롬브라우져에서 현재 불러온 소스 가져옴
soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정

########################### 그림파일 저장 ###########################

### 검색한 구글 이미지의 url을 따오는 코드 ###
def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="rg_i Q4LuWd")  # 구글 이미지 url 이 있는 img 태그의 _img 클래스에 가서 (f12로 확인가능.)
    for im in imgList:
        try :
            params.append(im["src"])                   # params 리스트에 image url 을 담음.
        except KeyError:
            params.append(im["data-src"])
    return params

# except부분
# 이미지의 상세 url 의 값이 있는 src 가 없을 경우
# data-src 로 가져오시오 ~  


def fetch_detail_url():
    params = fetch_list_url()

    for idx,p in enumerate(params,1):
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "C:/gimages/" + str(idx) + "_google.jpg")

# enumerate 는 리스트의 모든 요소를 인덱스와 쌍으로 추출
# 하는 함수 . 숫자 1은 인덱스를 1부터 시작해라 ~

fetch_detail_url()

# 끝나면 브라우져 닫기
browser.quit()




