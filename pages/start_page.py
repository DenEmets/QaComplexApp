from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_in(self, username, password):
        """Sign In as a user"""
        # Fill login, password
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)

        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    def verify_sign_in_error(self):
        """Verify invalid Sign In error"""
        assert self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH) == self.constants.SIGN_IN_LOGIN_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH)}"

    def sign_up_and_verify(self, username, email, password):
        """Sign Up as a user and verify that you are inside"""
        # Fill username, email, password
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        # Click button
        self.click_sign_up_and_verify()
        # Return new page
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    def sign_up(self, username, email, password, verify=True):
        """Sign Up as a user and verify that you are inside"""
        # Fill username, email, password
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)

        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

        # if verify:
        #     self.click_sign_up_and_verify()
        # else:
        #     self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @wait_until_ok(period=0.25)
    def click_sign_up_and_verify(self):
        """Click sign up button and verify"""
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_exists(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
