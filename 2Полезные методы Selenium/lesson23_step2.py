from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

 
link = " http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

alert = browser.switch_to.alert
alert_text = alert.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x) 
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
 

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()