# Solve reCaptcha V2 with Selenium Python Using 2captcha

from selenium import webdriver
import requests, time

API_KEY = "Your 2captcha API"
data_sitekey = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'
page_url ='https://www.google.com/recaptcha/api2/demo'

def Solver():
    driver = webdriver.Chrome()
    driver.get(page_url)
    u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
    r1 = requests.get(u1)
    print(r1.json())
    rid = r1.json().get("request")
    u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
    time.sleep(5)
    while True:
        r2 = requests.get(u2)
        print(r2.json())
        if r2.json().get("status") == 1:
            form_tokon = r2.json().get("request")
            break
        time.sleep(5)
    wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
    submit_js = 'document.getElementById("recaptcha-demo-form").submit();'
    driver.execute_script(wirte_tokon_js)
    time.sleep(3)
    driver.execute_script(submit_js)
    time.sleep(10)

if __name__ == '__main__':
    Solver()
