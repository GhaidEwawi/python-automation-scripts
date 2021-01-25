# Using Selenium to interact with web pages. 
# A custom driver for your current brower need to be installed. And it must be added to path variable.

from selenium import webdriver

# First Form
driver = webdriver.Edge()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('HelloWorld')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

# Second Form
aBox = driver.find_element_by_xpath('//*[@id="sum1"]')
bBox = driver.find_element_by_xpath('//*[@id="sum2"]')
aBox.send_keys('14')
bBox.send_keys('15')
showSumButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
showSumButton.click()