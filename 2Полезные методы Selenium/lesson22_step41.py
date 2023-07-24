from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("div.form-group :nth-child(2)")
input1.send_keys("1")

input2 = browser.find_element_by_css_selector("div.form-group :nth-child(4)")
input2.send_keys("2")

input3 = browser.find_element_by_css_selector("div.form-group :nth-child(6)")
input3.send_keys("3")


import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt') 
          # добавляем к этому пути имя файла 


input4 = browser.find_element_by_css_selector("input#file")   #ищем элемент Выбрать файл
input4.send_keys(file_path)

