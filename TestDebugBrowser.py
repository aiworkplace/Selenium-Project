from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


url = "http://www.google.com/"

opts = Options()
opts.add_experimental_option('debuggerAddress', 'localhost:9250')
driver = webdriver.Chrome(chrome_options=opts)
driver.get(url)

driver.find_element_by_name('q').send_keys('ArvanWorkhop - youtube')
driver.find_element_by_name("q").send_keys(Keys.ENTER)