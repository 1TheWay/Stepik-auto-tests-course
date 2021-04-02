from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_class_name('btn.btn-primary')
    submit.click()

    #time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    #time.sleep(1)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element_by_id('answer')
    input_1.send_keys(str(y))

    submit = browser.find_element_by_tag_name("button")
    submit.click()
finally:
    time.sleep(15)
    browser.quit()
