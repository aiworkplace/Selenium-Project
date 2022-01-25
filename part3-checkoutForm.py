import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'https://getbootstrap.com/docs/4.3/examples/checkout/'

driver = webdriver.Firefox()
driver.get(url)

time.sleep(2)
driver.find_element_by_id('firstName').send_keys("Ai")
time.sleep(2)
driver.find_element_by_id('lastName').send_keys("Workplace")
time.sleep(2)
driver.find_element_by_id('username').send_keys("Ai Workplace")
time.sleep(2)
driver.find_element_by_id('email').send_keys("aiworkplace701@gmail.com")
time.sleep(2)
driver.find_element_by_id('address').send_keys("Bell,Los Angeles")
time.sleep(2)

element = driver.find_element_by_id('country')
drp = Select(element)
drp.select_by_visible_text('United States')
time.sleep(2)
element = driver.find_element_by_id('state')
drp = Select(element)
drp.select_by_visible_text('California')
time.sleep(2)
driver.find_element_by_id('zip').send_keys("90201")

time.sleep(2)
driver.find_element_by_xpath('//*[@class="custom-control-label"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@for="paypal"]').click()

time.sleep(2)
driver.find_element_by_id('cc-name').send_keys("MasterCard")
time.sleep(2)
driver.find_element_by_id('cc-number').send_keys("5555555555554444")
time.sleep(2)
driver.find_element_by_id('cc-expiration').send_keys("0521")
time.sleep(2)
driver.find_element_by_id('cc-cvv').send_keys("000")
time.sleep(2)
driver.find_element_by_xpath('//*[@class="btn btn-primary btn-lg btn-block"]').click()
