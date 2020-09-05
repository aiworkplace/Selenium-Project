import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

url = 'https://www.google.com'

# Chrome Driver
driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_name('q').send_keys('Chrome Driver')
driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()


# FireFox Driver
driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_name('q').send_keys('FireFox Driver')
driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()

# Opera Driver
driver = webdriver.Opera()
driver.get(url)

driver.find_element_by_name('q').send_keys('Opera Driver')
driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()