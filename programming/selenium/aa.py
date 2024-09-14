from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
driver.get("http://www.python.org")
assert "Python" in driver.title
print(driver.title)
elem = driver.find_element_by_name("q")
print(elem)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
