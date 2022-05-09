from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    print(browser.switch_to.alert.text)
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла - UNIX/Linux ожидают пустую строку в конце файла, если в вашем
# скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться
