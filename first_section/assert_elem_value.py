from selenium import webdriver
import time

# директирия с проектом называется "stepik", в ней же находится файл драйвера хрома (chromedriver)
link = "http://suninjuly.github.io/registration1.html"
# для того, чтобы посмотреть как тест работает на 2й странице, стоит раскомментировать линк под комментарием
# и закоментировать верхний
# link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome("../stepik/chromedriver")

try:

    browser.get(link)

    input0 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input0.send_keys("Ivan")
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input1.send_keys("Petrov")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input2.send_keys("ma@am.ru")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
    input3.send_keys("778890")
    input4 = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
    input4.send_keys("address")
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

    sucess_element = browser.find_element_by_tag_name('h1')
    sucess_text = sucess_element.text
    assert "Congratulations! You have successfully registered!" == sucess_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
