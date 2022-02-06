from selenium import webdriver
import time
import pytest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
def test_text1():


    browser = webdriver.Chrome()
    browser.get(link1)

    input1 = browser.find_element_by_css_selector("input.form-control.first")
    input1.send_keys('alex')
    input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name'")
    input2.send_keys('yr')
    input3 = browser.find_element_by_css_selector("input.form-control.third")
    input3.send_keys('er@kk.ru')
 

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")    
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text
  

def test_text2():
    

    browser = webdriver.Chrome()
    browser.get(link2)

    input1 = browser.find_element_by_css_selector("input.form-control.first")
    input1.send_keys('alex')
    input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name'")
    input2.send_keys('yr')
    input3 = browser.find_element_by_css_selector("input.form-control.third")
    input3.send_keys('er@kk.ru')
    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")    
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text
  



if __name__ == "__main__":
    pytest.main()