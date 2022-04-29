from .base_page import BasePage
from .locators import YandexPageLocators

class SearchPage(BasePage):
    def should_be_search_form(self):
        assert self.is_element_present(YandexPageLocators.SEARCH_LINE), "The search string is missing!(Поисковая строка не найдена)"

    def should_be_search_suggest(self):
        assert self.is_element_present(YandexPageLocators.SUGGEST_VIEW), "The suggest is missing!(Suggest не найдена)"

    def should_be_search_table(self):
        assert self.is_element_present(YandexPageLocators.SEARCH_TABLE), "The searche table is missing!(Таблица с результатами поиска не найдена)"