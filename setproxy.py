from selenium import webdriver


myProxy = "116.206.47.54:8080"
ip, port = myProxy.split(":")
driver = webdriver.FirefoxProfile()
driver.set_preference('network.proxy.type', 1)
driver.set_preference('network.proxy.socks', ip)
driver.set_preference('network.proxy.socks_port', int(port))
driver = webdriver.Firefox(driver)
driver.get('https://whoer.net/')