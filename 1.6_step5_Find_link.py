from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/find_link_text"
txt = str(math.ceil(math.pow(math.pi, math.e)*10000))
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element_by_link_text(txt).click()

    browser.find_element_by_tag_name("input").send_keys("Ivan")
    browser.find_element_by_name('last_name').send_keys("Petrov")
    browser.find_element_by_class_name('city').send_keys("Smolensk")
    browser.find_element_by_id('country').send_keys("Russia")

    browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла