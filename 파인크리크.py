from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

import time
#파인크리크 매크로
driver = webdriver.Chrome()
login = 'https://www.tyleisure.co.kr/Tmember/index01.jsp'
reservation = ''
driver.get(login)

# 파인크리크 아이디 비밀번호 입력란
driver.find_element_by_name('oldMembNo').send_keys('@@@@@')
driver.find_element_by_name('passWd').send_keys('@@@@@')

#파인크리크 로그인 엔터
driver.find_element_by_name('passWd').send_keys(Keys.ENTER)

time.sleep(1)

#클릭버튼1
totalClick = driver.find_element_by_xpath(
    '//*[@id="contents"]/div/div/div[2]/div[2]/div[2]/img[1]')
totalClick.click()

time.sleep(1)

#클릭버튼2
pineCreekClick = driver.find_element_by_xpath(
    '//*[@id="crk"]')
pineCreekClick.click()

time.sleep(1)
