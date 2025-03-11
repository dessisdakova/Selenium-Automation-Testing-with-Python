from pages.exceptions_page import ExceptionsPage
from tests.conftest import driver


def test_no_such_element_exception(driver):
    ex_page = ExceptionsPage(driver)
    ex_page.load()
    ex_page.get_add_button(1).click()

    # assert ex_page.get_input_field(2)  # assertion fails with expected Exception
    assert ex_page.get_input_field_with_wait(2)


def test_element_not_interactable_exception(driver):
    ex_page = ExceptionsPage(driver)
    ex_page.load()
    ex_page.get_add_button(1).click()
    ex_page.get_input_field_with_wait(2).send_keys("Chocolate")

    assert ex_page.get_conformation_msg_text() == "Row 2 was added", "Incorrect confirmation message."


def test_invalid_element_state_exception(driver):
    ex_page = ExceptionsPage(driver)
    ex_page.load()
    ex_page.get_edit_button(1).click()  # remove for test to fail with expected Exception
    ex_page.get_input_field(1).clear()
    ex_page.get_save_button(1).click()

    assert ex_page.get_conformation_msg_text() == "Row 1 was saved", "Incorrect confirmation message."


def test_stale_element_reference_exception(driver):
    ex_page = ExceptionsPage(driver)
    ex_page.load()
    # label = ex_page.get_instructions_label()
    ex_page.get_add_button(1).click()

    # assert not label.is_displayed() # assertion fails with expected Exception
    assert ex_page.get_instructions_label_with_wait()
