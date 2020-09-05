from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = 'https://whoer.net/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'

driver = webdriver.Chrome()

opts = Options()
opts.add_argument("user-agent=" + user_agent)
driver = webdriver.Chrome(chrome_options=opts)
driver.get(url)