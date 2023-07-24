from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

link = " https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


a = browser.find_element(By.ID,'num1').text
b = browser.find_element(By.ID,'num2').text
c = str(int(a) + int(b))

select = Select(browser.find_element(By.ID,'dropdown'))
select.select_by_value(c)

input = browser.find_element(By.ID, "dropdown")
input.send_keys(c)


button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
    

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
