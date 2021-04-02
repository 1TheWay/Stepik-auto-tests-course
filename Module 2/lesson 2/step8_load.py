from selenium import webdriver
import time
import os

file = 'text.txt'
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла

with open(file, 'w') as f:
    text = '''Привет, Мир!'''
    f.write(text)

file_path = os.path.join(current_dir, file)           # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    fields = browser.find_elements_by_tag_name('input')
    [elem.send_keys('Data') for elem in fields[:3]]
    fields[3].send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
