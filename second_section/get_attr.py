from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome("/home/m/PycharmProjects/stepik/chromedriver")


try:

    browser.get(link)
    treasure_pic = browser.find_element_by_id("treasure")
    x = treasure_pic.get_attribute("valuex")

    answer_element = browser.find_element_by_id("answer")
    answer_element.send_keys(calc(x))

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