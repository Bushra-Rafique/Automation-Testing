from pages.login_page import LoginPage
from utils.config import Config

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate(Config.BASE_URL)
    login.submit_login(Config.USERNAME, Config.PASSWORD)

    assert "Logged In Successfully" in login.get_success_text()

def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate(Config.BASE_URL)
    login.submit_login("wrong_user", "wrong_pass")

    assert "Your username is invalid!" in login.get_error_text()