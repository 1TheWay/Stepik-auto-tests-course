from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)))
    submit_button = browser.find_element_by_tag_name("button")
    submit_button.click()
finally:
    time.sleep(15)
    browser.quit()
