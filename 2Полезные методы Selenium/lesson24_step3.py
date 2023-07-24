﻿from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
h5 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"),'$100')
    )

button = browser.find_element(By.CSS_SELECTOR, "#book")
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x) 


input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "#solve")
button.click()


time.sleep(40)
    # закрываем браузер после всех манипуляций
browser.quit()
