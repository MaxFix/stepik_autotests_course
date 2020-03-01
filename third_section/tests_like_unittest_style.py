from selenium import webdriver
import unittest


class TestForWebdriver(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_correct_link(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration1.html")

        input0 = driver.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        input0.send_keys("Ivan")
        input1 = driver.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        input1.send_keys("Petrov")
        input2 = driver.find_element_by_xpath('//input[@placeholder="Input your email"]')
        input2.send_keys("ma@am.ru")
        input3 = driver.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
        input3.send_keys("778890")
        input4 = driver.find_element_by_xpath('//input[@placeholder="Input your address:"]')
        input4.send_keys("address")
        button = driver.find_element_by_css_selector("button.btn-default")
        button.click()

        sucess_element = driver.find_element_by_tag_name('h1')
        sucess_text = sucess_element.text
        self.assertEqual("Congratulations! You have successfully registered!", sucess_text, 'Incorrect page element')

    def test_incorrect_link(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration2.html")

        input0 = driver.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        input0.send_keys("Ivan")
        input1 = driver.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        input1.send_keys("Petrov")
        input2 = driver.find_element_by_xpath('//input[@placeholder="Input your email"]')
        input2.send_keys("ma@am.ru")
        input3 = driver.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
        input3.send_keys("778890")
        input4 = driver.find_element_by_xpath('//input[@placeholder="Input your address:"]')
        input4.send_keys("address")
        button = driver.find_element_by_css_selector("button.btn-default")
        button.click()

        sucess_element = driver.find_element_by_tag_name('h1')
        sucess_text = sucess_element.text
        self.assertEqual("Congratulations! You have successfully registered!", sucess_text,
                         'Incorrect page element')

    def tearDown(self):  # закрываем браузер после всех манипуляций
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

