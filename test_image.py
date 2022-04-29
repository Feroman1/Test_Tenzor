import pytest
from .test_base.main_page import MainPage
from .test_base.image_page import ImagePage

FIRST_URL = 'https://yandex.ru/'
CORRECT_IMAGE_URL = 'https://yandex.ru/images/'
IMAGE_CATEGORY = 1
IMAGE_NUMBER = 1
def test_search_image(browser):
    page = MainPage(browser, FIRST_URL)
    page.open()
    ImagePage.should_be_search_image_form(page)
    page.go_to_image_box()
    ImagePage.should_be_correct_url(browser, CORRECT_IMAGE_URL)
    page.go_to_category(IMAGE_CATEGORY)
    page.go_to_image(IMAGE_NUMBER)

if __name__ == "__main__":
    pytest.main()