from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    username_file = (By.CSS_SELECTOR, "div > input[id='username']")
    password_field = (By.CSS_SELECTOR, "div > input[id='password']")
    submit_btn = (By.CSS_SELECTOR, "button[id='submit']")
    logout_btn = (By.XPATH, "//*[@id='loop-container']/div/article/div[2]/div/div/div/a)")
    error_msg = (By.CSS_SELECTOR, "div[id='error']")

    @property
    def url(self):
        return super().url + "/practice-test-login"

    def login(self, username: str, password: str):
        self._driver.find_element(*LoginPage.username_file).send_keys(username)
        self._driver.find_element(*LoginPage.password_field).send_keys(password)
        self._driver.find_element(*LoginPage.submit_btn).click()

    def get_visibility_of_logout_btn(self):
        return self._driver.find_element(LoginPage.logout_btn).is_displayed()

    def get_error_msg_text(self):
        return self._driver.find_element(*LoginPage.error_msg).text
