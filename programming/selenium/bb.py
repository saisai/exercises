#!/usr/bin/env python
# coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browserName': 'iPhone',
 'device': 'iPhone 7',
 'realMobile': 'true',
 'os_version': '10.3'
}

desired_cap = {
 'browserName': 'firefox',
 'device': 'Mozilla Firefox 61.0.1',
 'realMobile': 'false',
 'os_version': '61.0.1'
}

desired_cap = {
 'browser': 'chromedriver',
 'browser_version': '2.40',
 'os': 'Linux', 
}

# System info: host: 'localhost', ip: '127.0.0.1', os.name: 'Linux', os.arch: 'amd64', os.version: '4.17.8-1-ARCH', java.version: '1.8.0_172'
'''
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'firefox',
                         'version': '2',
                        'javascriptEnabled': True})   
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)      

driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.PHANTOMJS)  
'''
driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   desired_capabilities={'acceptInsecureCerts': True, 'browserName': 'firefox', 'marionette': True})   

driver.get("http://google.com")

#elem = driver.find_element_by_name("q")
#elem.send_keys("BrowserStack")
#elem.submit()
print(driver.title)

#driver.get("http://www.google.com")
driver.get_screenshot_as_file('google.png')
driver.quit()

driver.quit()

