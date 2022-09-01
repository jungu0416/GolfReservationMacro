from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

import time
#한원컨트리클럽 매크로
driver = webdriver.Chrome()
login = 'https://www.hanwoncc.co.kr/login/login.asp'
reservation = 'https://www.hanwoncc.co.kr/Login/Login.asp?strPrevURL=/reservation/waiting.asp'
driver.get(reservation)

# 한원컨트리클럽 아이디 비밀번호 입력란
driver.find_element_by_css_selector('#MN_Log_M1').send_keys('@@')
driver.find_element_by_css_selector('#MN_Log_M2').send_keys('@@@@@')
driver.find_element_by_css_selector('#MP_Log_M1').send_keys('@@@@@')

#한원컨트리클럽 로그인 엔터
driver.find_element_by_css_selector('#MP_Log_M1').send_keys(Keys.ENTER)

time.sleep(1)

Alert(driver).accept()

#여기서부턴 대기예약임;

#셀렉트 박스 핸들링 날짜 
selectDate = Select(driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/div/form/table/tbody/tr[2]/td[4]/select'))
selectDate.select_by_index(3)

#셀렉트 박스 핸들링 시간
selectTime = Select(driver.find_element_by_xpath(
    '/html/body/div/div[2]/div[2]/div[2]/div[2]/div/form/table/tbody/tr[2]/td[5]/select'))
selectTime.select_by_index(4)


#클릭버튼
#finalClick = driver.find_element_by_css_selector('.waiting_btn02')
#finalClick.click()

#time.sleep(1)

#Alert(driver).accept()
