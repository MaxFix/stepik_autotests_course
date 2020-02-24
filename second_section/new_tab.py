from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser.get(link)

    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    answer_element = browser.find_element_by_id("answer")
    answer_element.send_keys(calc(x))

    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
