from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))




link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn-primary').click()

finally:
    print(browser.switch_to.alert.text)
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
