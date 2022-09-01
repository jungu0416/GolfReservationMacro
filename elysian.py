from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException,NoSuchElementException, TimeoutException, ElementNotInteractableException, NoSuchWindowException, NoSuchFrameException

import sys
import os
import time

# pyinstaller --add-binary "chromedriver.exe";"." elysian.py
#python 크롬드라이버랑 같이 exe파일 만들기
if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

#엘리시안강촌 매크로
login = 'https://www.elysian.co.kr/member/login.asp?return_url_yn=Y&return_url=/reservation/golf.asp'
driver.get(login)

# 엘리시안강촌 아이디 비밀번호 입력란
driver.find_element_by_css_selector(
    '#userinfo01_01').send_keys('@@@@@')
driver.find_element_by_css_selector(
    '#userinfo01_02').send_keys('@@@@@')

#엘리시안강촌 로그인 엔터
driver.find_element_by_css_selector(
    '#userinfo01_02').send_keys(Keys.ENTER)

#엘리시안강촌 다음달 달력 표시
driver.execute_script("javascript:fnGetMonth('+');")

#엘리시안강촌 1.날짜선택
#fnChoiceDate(this, '2022-05-29', 'POSS')
#엘리시안강촌 2. 코스/시간선택

#엘리시안강촌 달력 행
rows = 1
#엘리시안강촌 달력 열 
cols = 2
#엘리시안강촌 예약 확정된 횟수
cnt = 0

#코스/시간 선택
course = 1;
courseTime = 1;



while rows <= 5:
    while cols <= 6:
        try:
            driver.find_element_by_xpath(
                '//*[@id="divGolfCal"]/div[2]/table/tbody/tr['+str(rows)+']/td['+str(cols)+']/a').click()
            Alert(driver).accept()
            print('예약못하는 부분 : 행 -> ' + str(rows) + ' 열 -> ' + str(cols))
        except NoSuchElementException:
            print('달력에 해당 element가 없음 : 행 -> ' + str(rows) + ' 열 -> ' + str(cols))
        except NoAlertPresentException:
            print('예약가능 : 행 -> ' + str(rows) + ' 열 -> ' + str(cols))
            #코스 클릭


            #try 이전에 while로 다 돌려보기
            try:
                driver.find_element_by_xpath(
                    '//*[@id="divGolfCourseTime2"]/div['+str(course)+']/ul/li['+str(courseTime)+']').click()

                Alert(driver).accept()
                print('코스/시간 선택 버튼 눌렀는데 alert뜸')
            except NoSuchElementException:
                print('예약가능 시간 없음')
            except NoAlertPresentException:
                print('alert창 안뜨니깐 이제 로직 여기서 부터 만들면 됨');

                #엘리시안강촌 동의함 클릭
                #driver.find_element_by_id('golfAgreeY').click()

                #엘리시안강촌 예약 클릭
                #driver.execute_script('fnReservation()')

        cols += 2
    
    cols = 2
    rows += 1

