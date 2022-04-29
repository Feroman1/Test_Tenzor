from .base_page import BasePage
from test_base.locators import YandexPageLocators, ImagePageLocators
from .search_page import SearchPage
from selenium.webdriver.common.by import By
from .image_page import ImagePage



class MainPage(BasePage):
    def go_to_search_line(self, search_text):
        login_link = self.browser.find_element(*YandexPageLocators.SEARCH_LINE)
        login_link.send_keys(search_text)
        return SearchPage(browser=self.browser, url=self.browser.current_url)

    def press_button(self, button_name):
        login_link = self.browser.find_element(*YandexPageLocators.SEARCH_LINE)
        login_link.send_keys(button_name)

    def required_site(self, browser, link, amount):
        """
        Explore links and find the right one
        """
        links = browser.find_elements_by_css_selector('#search-result > .serp-item a.link > b')
        items = [elem.text.strip() for elem in links[:amount]]
        if link not in items:
            raise Exception(f'сайта {link} нет в первых {amount} пунктах')

    def go_to_image_box(self):
        """
        Open Image and switch window
        """
        self.browser.find_element(*ImagePageLocators.IMAGE_BOX).click()
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(window_name=new_window)

    def go_to_category(self, category):
        """
        Open  {category} and compare the text in the search bar
        """
        category_link = self.browser.find_element(By.CSS_SELECTOR, f'.PopularRequestList-Item_pos_{category - 1}')
        category_link_text = category_link.text
        category_link.click()
        ImagePage.should_be_search_line(self)
        line_inscription = self.browser.find_element(*ImagePageLocators.CATEGORY_LINK).get_attribute('value')
        assert (line_inscription == category_link_text), "Строка поиска не совпадает с категорией"

    def go_to_image(self, number):
        """
        Open {number} image and compare different src
        """
        self.browser.find_element(By.CSS_SELECTOR, f'.serp-item_pos_{number - 1}').click()
        ImagePage.should_be_open_image(self)
        firstimage_src = self.browser.find_element(*ImagePageLocators.CENTER_IMAGE).get_attribute('src')
        self.browser.find_element(*ImagePageLocators.NEXT_BUTTON).click()
        ImagePage.should_be_open_image(self)
        secondimage_src = self.browser.find_element(*ImagePageLocators.CENTER_IMAGE).get_attribute('src')
        assert (firstimage_src != secondimage_src), "The same photo(То же самое фото)"
        self.browser.find_element(*ImagePageLocators.PREV_BUTTON).click()
        ImagePage.should_be_open_image(self)
        previmage_src = self.browser.find_element(*ImagePageLocators.CENTER_IMAGE).get_attribute('src')
        assert (firstimage_src == previmage_src), "Different images(Разные фото)"