
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
import sys
 
driver = webdriver.Chrome()
url = 'https://ccmc.gsfc.nasa.gov/modelweb/models/nrlmsise00.php'
driver.get(url)
action = ActionChains(driver)

#function (Do not change anything)
def month(num) :
    select = Select(driver.find_element_by_name('month'))
    select.select_by_index(index=num-1)
ttt=''
def latitude(num) :
    global ttt #for filename
    t=num+90
    ttt=str(t).zfill(3) 
    driver.find_element_by_name("latitude").click()
    action.send_keys(Keys.BACKSPACE)
    action.send_keys(Keys.BACKSPACE)
    action.send_keys(Keys.BACKSPACE)
    action.send_keys(num).perform()
    time.sleep(1)
ggg=''
def longitude(num) :
    global ggg #for filename
    ggg=str(num).zfill(3)
    driver.find_element_by_name("longitude").click()
    action.send_keys(Keys.BACKSPACE)
    action.send_keys(Keys.BACKSPACE)
    action.send_keys(Keys.BACKSPACE)
    action.send_keys(num).perform()
    time.sleep(1)  
  #longitude 10~360
def repeat() :
    for i in range(10,370,10):
        driver.back()
        longitude(i)
        sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
        driver.find_element_by_css_selector("input[type='submit']").click()
        print(soup.find('pre').get_text())



#foldername
foldername='20190215/'

#year
yyyy='2019' #for filename
driver.find_element_by_name("year").click()
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys("2019").perform()

#month
mm='02' #for filename (ex:01,02,03....12)
month(2) #(ex: 1,2,3...12)
time.sleep(1)

#day
dd='15' #for filename
driver.find_element_by_name("day").click()
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys("15").perform()
time.sleep(1)

#latitude
latitude(0)

#longitude
longitude(0)

#stepsize
driver.find_element_by_name("step").click()
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys(Keys.BACKSPACE)
action.send_keys("10").perform() #step size
time.sleep(1)

#checkbox
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[1]/table/tbody/tr[3]/td/input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[1]/table/tbody/tr[4]/td/input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[1]/table/tbody/tr[5]/td/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[2]/table/tbody/tr[1]/td//input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[2]/table/tbody/tr[2]/td//input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[2]/table/tbody/tr[3]/td//input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[2]/table/tbody/tr[4]/td//input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[2]/table/tbody/tr[5]/td//input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[4]/th[2]/table/tbody/tr[6]/td//input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[6]/th[1]/table/tbody/tr[1]/td//input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[6]/th[1]/table/tbody/tr[2]/td//input").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/table[1]/tbody/tr[6]/th[1]/table/tbody/tr[3]/td//input").click()
time.sleep(1)

#filename
sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')

#submit
driver.find_element_by_css_selector("input[type='submit']").click()
html=driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.find('pre').get_text())


#restart

#repeat()

# driver.back()
# latitude(-80)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(-70)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(-60)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(-50)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(-40)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(-30)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(-20)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(-10)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(0)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(10)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(20)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(30)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(40)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(50)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(60)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(70)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(80)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

# driver.back()
# latitude(90)
# longitude(0)
# sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
# driver.find_element_by_css_selector("input[type='submit']").click()
# html=driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('pre').get_text())
# repeat()

#################################################

#Loop firsttime
#latitude -80~90 #longitude 10~360
for j in range(-90,100,10):
    driver.back()
    latitude(j)
    longitude(0)
    sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
    driver.find_element_by_css_selector("input[type='submit']").click()
    print(soup.find('pre').get_text())
    for i in range(10,370,10):
        driver.back()
        longitude(i)
        sys.stdout=open(foldername+yyyy+mm+dd+ttt+ggg+'.txt','w')
        driver.find_element_by_css_selector("input[type='submit']").click()
        print(soup.find('pre').get_text())


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