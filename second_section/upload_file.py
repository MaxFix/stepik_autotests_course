from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()


try:

    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_name("email")
    email.send_keys("Ivan@petrov.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    upload_btn = browser.find_element_by_id("file")
    upload_btn.send_keys(file_path)

    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
