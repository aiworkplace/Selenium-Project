from selenium import webdriver




myProxy = "13.55.51.101:8080"

ip, port = myProxy.split(":")
driver = webdriver.FirefoxProfile()
driver.set_preference('network.proxy.type', 1)
driver.set_preference('network.proxy.socks', ip)
driver.set_preference('network.proxy.socks_port', int(port))
driver = webdriver.Firefox(driver)

driver.get('https://whoer.net/')