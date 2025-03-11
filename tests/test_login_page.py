import pytest

from pages.login_page import LoginPage


def test_successful_login(driver):
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("student", "Password123")

    assert expected_url == login_page.get_current_url() , "User is not redirected to expected page."
    assert login_page.get_current_url(), "Logout button is not present."


@pytest.mark.parametrize("username, password, expected_mgs",
                         [("incorrectUser", "Password123", "Your username is invalid!"),
                          ("student", "incorrectPassword", "Your password is invalid!")])
def test_unsuccessful_login(driver, username, password, expected_mgs):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    assert login_page.get_error_msg_text() == expected_mgs, "Error message does not match expected."