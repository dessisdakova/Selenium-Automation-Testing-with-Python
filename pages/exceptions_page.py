from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class ExceptionsPage(BasePage):

    @property
    def url(self):
        return super().url + "/practice-test-exceptions"

    def _get_element(self, row_number, locator_type, locator_value):
        """Helper method to construct locators and find elements."""
        locator = (locator_type, locator_value.replace("row1", f"row{row_number}"))
        return self._driver.find_element(*locator)

    def get_input_field(self, row_number):
        return self._get_element(row_number, By.CSS_SELECTOR, "div[id='row1'] > input[type='text']")

    def get_add_button(self, row_number):
        return self._get_element(row_number, By.CSS_SELECTOR, "div[id='row1'] > button[id='add_btn']")

    def get_edit_button(self, row_number):
        return self._get_element(row_number, By.CSS_SELECTOR, "div[id='row1'] > button[id='edit_btn']")

    def get_save_button(self, row_number):
        return self._get_element(row_number, By.CSS_SELECTOR, "div[id='row1'] > button[id='save_btn']")

    def get_conformation_msg_text(self):
        return self._driver.find_element(By.CSS_SELECTOR, "div[id='confirmation']").text

    def _wait_for_element_to_be_present(self, row_number, locator_type, locator_value, timeout=6):
        """Helper method to wait for element presence."""
        locator = (locator_type, locator_value.replace("row1", f"row{row_number}"))
        return WebDriverWait(self._driver, timeout).until(ec.presence_of_element_located(locator))

    def get_input_field_with_wait(self, row_number, timeout=6):
        return self._wait_for_element_to_be_present(row_number,
                                                    By.CSS_SELECTOR,
                                      "div[id='row1'] > input[type='text']", timeout)

    def get_instructions_label(self):
        return self._driver.find_element(By.CSS_SELECTOR, "section > p[id='instructions']")

    def get_instructions_label_with_wait(self):
        """Wait for element to be invisible."""
        return (WebDriverWait(self._driver, 5).
                until(ec.invisibility_of_element((By.CSS_SELECTOR, "section > p[id='instructions']"))))
