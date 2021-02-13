from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = 'https://www.instagram.com/'
driver.get(url)
action = ActionChains(driver)

driver.find_element_by_name("username").click()
action.send_keys("seoulfromseoul").perform()

driver.find_element_by_name("username").click()
action.send_keys("password99").perform()
