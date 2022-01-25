from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def send_delayed_keys(element, text, delay=0.4):
    for c in text:
        endtime = time.time() + delay
        element.send_keys(c)
        time.sleep(endtime - time.time())

url = "http://www.google.com/"
driver = webdriver.Chrome()
driver.get(url)


kyes = driver.find_element_by_name('q')
send_delayed_keys(kyes, 'Ai Workplace - youtube', 0.6)
driver.find_element_by_name("q").send_keys(Keys.ENTER)
