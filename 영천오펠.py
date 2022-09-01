from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

import time
#영천오펠 매크로
driver = webdriver.Chrome()
login = 'https://www.ophelgc.com/_YeongCheon/Member/Login.aspx'
reservation = ''
driver.get(login)

# 영천오펠 아이디 비밀번호 입력란
driver.find_element_by_css_selector(
    '#ctl00_contents_LoginControl_UserID').send_keys('@@@@@')
driver.find_element_by_css_selector(
    '#ctl00_contents_LoginControl_UserPassword').send_keys('@@@@@')

#영천오펠 로그인 엔터
driver.find_element_by_css_selector(
    '#ctl00_contents_LoginControl_UserPassword').send_keys(Keys.ENTER)
