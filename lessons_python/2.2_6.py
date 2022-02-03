import time
from tkinter import Button
from selenium import webdriver
import math
try:

    browser = webdriver.Chrome()
    link = ('http://suninjuly.github.io/execute_script.html')
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    button = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    y_radiobutton = browser.find_element_by_id('robotsRule').click()
    x_checkbox = browser.find_element_by_id('robotCheckbox').click()
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    print(y)
    searh = browser.find_element_by_id('answer')
    searh.send_keys(y)
    
    #scroll from object
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()