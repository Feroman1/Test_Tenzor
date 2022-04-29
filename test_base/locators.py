from selenium.webdriver.common.by import By

class YandexPageLocators():
    SEARCH_LINE = (By.XPATH, '//input[@id="text"]')
    SUGGEST_VIEW = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_tile.mini-suggest__popup_visible')
    SEARCH_TABLE = (By.CLASS_NAME, 'serp-list_left_yes')


class ImagePageLocators():
    IMAGE_BOX = (By.XPATH, '//li/a/div[text() = "Картинки"]')
    CATEGORY_LINK = (By.XPATH, '//input[@class ="input__control mini-suggest__input"]')
    CENTER_IMAGE = (By.XPATH, '//img[@class = "MMImage-Preview"]')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button')
    PREV_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button')