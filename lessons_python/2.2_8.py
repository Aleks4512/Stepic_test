from selenium import webdriver
import os
import time

link = ('http://suninjuly.github.io/file_input.html')
try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Alex')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Yr')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('qwer@ty.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'qwer.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_xpath('//*[@id="file"]')
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(30)
    browser.quit()