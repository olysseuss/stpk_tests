import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# определяем текущую директорию
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "example.txt"
# определяем путь к файлу
file_path = os.path.join(current_dir, file_name)

link2 = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector('[name="firstname"][required=""]').send_keys("Petrik")
    browser.find_element_by_css_selector('[name="lastname"][required=""]').send_keys("Piatochkin")
    browser.find_element_by_css_selector('[name="email"][required=""]').send_keys("Petrik@5.com")

    # загружаем файл
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

finally:
    print(browser.switch_to.alert.text)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()