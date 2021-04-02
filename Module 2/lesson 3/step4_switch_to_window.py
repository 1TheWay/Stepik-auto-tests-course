from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_class_name('trollface')
    submit.click()

    #time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
