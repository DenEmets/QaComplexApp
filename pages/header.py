from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.create_post_page import CreatePostPage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()

    def navigate_to_create_post_page(self):
        """Click on create post button"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        return CreatePostPage(self.driver)
