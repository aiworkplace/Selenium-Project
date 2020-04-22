import time
from selenium import webdriver


url = 'https://www.google.com'  # Choose your url or website link.


driver = webdriver.Chrome()     # connect your chromedriver.exe (note: selenium_fundamental.py and chromedriver.exe are same folder)
driver.get(url)                 # start

time.sleep(4)   # time Duration

driver.find_element_by_id('gb_70').click()
# here driver.find_element_by_id mean - you find your element by id
# click() --- mean press click this specific id.

time.sleep(4)

driver.find_element_by_name('identifier').send_keys('arvanbishwas@gmail.com')
# here driver.find_element_by_name mean - you find your element by name
# send_keys .. mean(hare you write any key) those key are send your element plase

time.sleep(4)

driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
# here driver.find_element_by_xpath mean - you find your element by class or any html content you went.



