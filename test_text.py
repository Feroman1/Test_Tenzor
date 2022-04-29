import pytest
from .test_base.main_page import MainPage
from .test_base.search_page import SearchPage
from selenium.webdriver.common.keys import Keys

FIRST_URL = 'https://yandex.ru/'
SEARCH_WORD = 'Тензор'
SEARCH_URL = 'tensor.ru'
AMOUNT_URL = 5

def test_search_tenzor(browser):
    page = MainPage(browser, FIRST_URL)
    page.open()
    SearchPage.should_be_search_form(page)
    page.go_to_search_line(SEARCH_WORD)
    SearchPage.should_be_search_suggest(page)
    page.press_button(Keys.ENTER)
    SearchPage.should_be_search_table(page)
    page.required_site(browser, SEARCH_URL, AMOUNT_URL)

if __name__ == "__main__":
    pytest.main()
#    search_page.should_be_search_form()