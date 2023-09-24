from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver import FirefoxOptions

desired_caps = {'platform': 'LINUX', 'browserName': 'firefox', 'version': '61.0',
    "screen-resolution" : "2560x1600"
 }

#driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=desired_caps)

driver.get("http://www.facebook.com")
driver.get_screenshot_as_file('google.png')
print(driver.title)
driver.quit()


# https://testingbot.com/support/other/test-options#screenresolution
# https://testingbot.com/support/getting-started/pyunit.html
# http://192.168.1.123:4444/wd/hub/static/resource/hub.html
# http://selenium-python.readthedocs.io/getting-started.html