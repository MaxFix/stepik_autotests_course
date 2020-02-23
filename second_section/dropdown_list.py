from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html" # first dropdown
#link = "http://suninjuly.github.io/selects2.html" # second variant dropdown

browser = webdriver.Chrome("/home/m/PycharmProjects/stepik/chromedriver")


try:

    browser.get(link)
    number1 = browser.find_element_by_id("num1")
    number1 = number1.text
    n1 = int(number1)
    number2 = browser.find_element_by_id("num2")
    number2 = number2.text
    n2 = int(number2)
    summa = n1 + n2

    drop_list = browser.find_element_by_id("dropdown")
    drop_list.click()

    select = Select(browser.find_element_by_tag_name("select"))
    expected_elem = select.select_by_value(str(summa))  # ищем элемент с текстом "Python"

    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
