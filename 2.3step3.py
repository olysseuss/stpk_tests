from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element_by_class_name('btn-primary').click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_class_name('btn-primary').click()

finally:
    print(browser.switch_to.alert.text)
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла