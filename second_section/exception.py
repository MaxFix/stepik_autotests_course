from selenium import webdriver
import time

browser = webdriver.Chrome()

try:

    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)

    browser.find_element_by_id("button")
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()