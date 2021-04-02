from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_tag_name('img')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input_1 = browser.find_element_by_id('answer')
    input_1.send_keys(str(y))
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    submit_button = browser.find_element_by_tag_name("button")
    submit_button.click()
finally:
    time.sleep(15)
    browser.quit()
