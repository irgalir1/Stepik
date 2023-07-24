from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
 
link = " http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

    # Ваш код, который заполняет обязательные поля
input1 = browser.find_element(By.XPATH, '//label[contains(text(),"First name*")]/following::input[1]')
input1.send_keys("Ivan")
input2 = browser.find_element(By.XPATH, '//label[contains(text(),"Last name*")]/following::input[1]')
input2.send_keys("Petrov")
input3 = browser.find_element(By.XPATH, '//label[contains(text(),"Email *")]/following::input[1]')
input3.send_keys("1@bk.ru")

    
current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, '11.txt')
input5 = browser.find_element(By.ID, 'file').send_keys(file_path)
	

    # Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
time.sleep(1)

    


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()