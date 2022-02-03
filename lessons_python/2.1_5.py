from os import link
import time
from tkinter import Button
from selenium import webdriver
import math
try:

    browser = webdriver.Chrome()
    link = ('http://suninjuly.github.io/math.html')
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    y_radiobutton = browser.find_element_by_id('robotsRule').click()
    x_checkbox = browser.find_element_by_id('robotCheckbox').click()
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    searh = browser.find_element_by_id('answer')
    searh.send_keys(y)

    button = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(30)
    browser.quit()
