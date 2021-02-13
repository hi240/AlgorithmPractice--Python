from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import time
import sys

driver = webdriver.Chrome()
url = 'https://www.instagram.com/'
driver.get(url)
action = ActionChains(driver)

driver.get('https://www.instagram.com/seoulfromseoul')
driver.execute_script("document.querySelectorAll('.-nal3')[1].click();")

time.sleep(2)

driver.find_element_by_name('username').send_keys('seoulfromseoul')
driver.find_element_by_name('password').send_keys(' ')

driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').submit()

time.sleep(5)

driver.execute_script("document.querySelectorAll('.-nal3')[1].click();")
time.sleep(1)
oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = driver.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    driver.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
followers = soup.findAll('a',['FPmhX','notranslate','_0imsa'])
followers_text = []
for follower in followers:
    followers_text.append(follower.get_text())
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()

time.sleep(0.5)

driver.execute_script("document.querySelectorAll('.-nal3')[2].click();")

time.sleep(1)

oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = driver.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    driver.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
followings = soup.findAll('a',['FPmhX','notranslate','_0imsa'])
followings_text = []
for following in followings:
    followings_text.append(following.get_text())

print("팔로잉 수: " + str(len(followings_text)))

result = []
for following in followings_text:
    cnt = 0
    for follower in followers_text:
        if following == follower:
            cnt += 1
            break
    if cnt == 0:
        result.append(following)

print('맞팔되지 못한 사람 목록: '+str(result))

class Keys(object):
    """
    Set of special keys codes.
    """

    NULL = '\ue000'
    CANCEL = '\ue001'  # ^break
    HELP = '\ue002'
    BACKSPACE = '\ue003'
    BACK_SPACE = BACKSPACE
    TAB = '\ue004'
    CLEAR = '\ue005'
    RETURN = '\ue006'
    ENTER = '\ue007'
    SHIFT = '\ue008'
    LEFT_SHIFT = SHIFT
    CONTROL = '\ue009'
    LEFT_CONTROL = CONTROL
    ALT = '\ue00a'
    LEFT_ALT = ALT
    PAUSE = '\ue00b'
    ESCAPE = '\ue00c'
    SPACE = '\ue00d'
    PAGE_UP = '\ue00e'
    PAGE_DOWN = '\ue00f'
    END = '\ue010'
    HOME = '\ue011'
    LEFT = '\ue012'
    ARROW_LEFT = LEFT
    UP = '\ue013'
    ARROW_UP = UP
    RIGHT = '\ue014'
    ARROW_RIGHT = RIGHT
    DOWN = '\ue015'
    ARROW_DOWN = DOWN
    INSERT = '\ue016'
    DELETE = '\ue017'
    SEMICOLON = '\ue018'
    EQUALS = '\ue019'

    NUMPAD0 = '\ue01a'  # number pad keys
    NUMPAD1 = '\ue01b'
    NUMPAD2 = '\ue01c'
    NUMPAD3 = '\ue01d'
    NUMPAD4 = '\ue01e'
    NUMPAD5 = '\ue01f'
    NUMPAD6 = '\ue020'
    NUMPAD7 = '\ue021'
    NUMPAD8 = '\ue022'
    NUMPAD9 = '\ue023'
    MULTIPLY = '\ue024'
    ADD = '\ue025'
    SEPARATOR = '\ue026'
    SUBTRACT = '\ue027'
    DECIMAL = '\ue028'
    DIVIDE = '\ue029'

    F1 = '\ue031'  # function  keys
    F2 = '\ue032'
    F3 = '\ue033'
    F4 = '\ue034'
    F5 = '\ue035'
    F6 = '\ue036'
    F7 = '\ue037'
    F8 = '\ue038'
    F9 = '\ue039'
    F10 = '\ue03a'
    F11 = '\ue03b'
    F12 = '\ue03c'

    META = '\ue03d'
    COMMAND = '\ue03d'