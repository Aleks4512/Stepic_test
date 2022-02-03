from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:


    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    sumx_y = int(x)+int(y)
    sumx_y1 = str(sumx_y)
    print(sumx_y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sumx_y1)

    button = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(30)
    browser.quit()
