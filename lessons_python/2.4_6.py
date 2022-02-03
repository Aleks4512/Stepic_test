from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "100"))
button.click()

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
x = x_element.text
y = calc(x)
searh = browser.find_element_by_id('answer')
searh.send_keys(y)

button1 = browser.find_element_by_id('solve').click()
