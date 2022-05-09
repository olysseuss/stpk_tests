from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector('[class="form-control first"][required=""]').send_keys("Petrik")
    browser.find_element_by_css_selector('[class="form-control second"][required=""]').send_keys("Piatochkin")
    browser.find_element_by_css_selector('[class="form-control third"][required=""]').send_keys("Petrik@5.com")

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = browser.find_element_by_tag_name("h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

