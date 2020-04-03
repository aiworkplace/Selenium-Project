import xlrd
import time
import pandas as pd
from selenium import webdriver

class Excel():
    def __init__(self):
        pass
    def reademail(self, dataPath):
        data = pd.read_excel(dataPath, 'Sheet1')
        df = data.to_dict()
        return df

dataPath = "data.xlsx"
reademail = Excel()
dataList = reademail.reademail(dataPath)
l = len(dataList['username'])

for i in range(l):
    temp = {
        'firstName': dataList['firstName'][i],
        'lastName': dataList['lastName'][i],
        'username': dataList['username'][i],
        'email': dataList['email'][i],
        'address': dataList['address'][i]
    }

    url = 'https://getbootstrap.com/docs/4.3/examples/checkout/'

    driver = webdriver.Firefox()
    driver.get(url)

    time.sleep(2)
    driver.find_element_by_id('firstName').send_keys(dataList['firstName'][i])
    time.sleep(2)
    driver.find_element_by_id('lastName').send_keys(dataList['lastName'][i])
    time.sleep(2)
    driver.find_element_by_id('username').send_keys(dataList['username'][i])
    time.sleep(2)
    driver.find_element_by_id('email').send_keys(dataList['email'][i])
    time.sleep(2)
    driver.find_element_by_id('address').send_keys(dataList['address'][i])
    time.sleep(2)
    driver.quit()
    print("Start Again")