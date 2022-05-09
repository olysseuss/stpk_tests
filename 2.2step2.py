from selenium import webdriver
import time


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    print(x+y)

    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector(f"[value='{str(int(x)+int(y))}']").click()
    browser.find_element_by_class_name('btn-default').click()

finally:
    print(browser.switch_to.alert.text)
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
