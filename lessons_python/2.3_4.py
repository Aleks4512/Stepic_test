from selenium import webdriver
import time
import math

link = ('http://suninjuly.github.io/alert_accept.html')
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.btn').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    searh = browser.find_element_by_id('answer')
    searh.send_keys(y)

    button = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(30)
    browser.quit()