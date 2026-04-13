class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators (Better than simple strings)
        self._username = page.locator("#username")
        self._password = page.locator("#password")
        self._login_btn = page.locator("#submit")
        self._success_msg = page.locator(".post-title")
        self._error_msg = page.locator("#error")

    def navigate(self, url):
        self.page.goto(url)

    def submit_login(self, user, pwd):
        self._username.fill(user)
        self._password.fill(pwd)
        self._login_btn.click()

    def get_success_text(self):
        return self._success_msg.text_content()

    def get_error_text(self):
        return self._error_msg.text_content()