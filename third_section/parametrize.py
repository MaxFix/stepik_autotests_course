import pytest
import time
import math
from selenium import webdriver


def get_time():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['236895', "236896", "236897", "236898",
                                  "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link):
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)
    answer_field = browser.find_element_by_css_selector('.textarea')
    answer_field.send_keys(str(get_time()))
    sbmt_btn = browser.find_element_by_css_selector('.submit-submission')
    sbmt_btn.click()

    hint_message = browser.find_element_by_css_selector('.smart-hints__hint')  # find message of optional feedback
    assert hint_message.text == 'Correct!', 'Fail in test on page {}'.format(link)  # compare with expexted answer
