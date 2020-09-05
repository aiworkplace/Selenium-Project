from selenium import webdriver

### HTTP Proxy
myProxy = '184.185.236.73:59422'
ip, port = myProxy.split(":")
driver = webdriver.FirefoxProfile()
driver.set_preference('network.proxy.type', 1)
driver.set_preference('network.proxy.http', ip)
driver.set_preference('network.proxy.http_port', int(port))
driver.set_preference("network.proxy.share_proxy_settings", True)
driver.set_preference("network.http.use-cache", False)
driver.update_preferences()
driver = webdriver.Firefox(firefox_profile=driver)

driver.get('https://www.youtube.com/channel/UCiKuwqQKQHRN3O-CaZmyppw/videos')