from .base_page import BasePage
from .locators import ImagePageLocators


class ImagePage(BasePage):
    def should_be_search_image_form(self):
        assert self.is_element_present(ImagePageLocators.IMAGE_BOX), "The image box not found!(Ссылка на картинки не найдена)"

    def should_be_correct_url(self, correct_url):
        assert (correct_url in self.current_url), f'В открытой сыллке отсутсвует {correct_url}'

    def should_be_search_line(self):
        assert self.is_element_present(ImagePageLocators.CATEGORY_LINK), "The searc bar not found!(поисковая строка не найдена)"

    def should_be_open_image(self):
        assert self.is_element_present(ImagePageLocators.CENTER_IMAGE), "The first image not found!(Первое фото не появилось)"