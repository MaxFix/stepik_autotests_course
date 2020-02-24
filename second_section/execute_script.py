from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()


try:

    browser.get(link)
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text

    value_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", value_field)
    value_field.send_keys(calc(x))

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobtn = browser.find_element_by_id("robotsRule")
    radiobtn.click()

    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
