from holmium.core import Page, Element, Locators


class LoginPage(Page):
    username = Element(Locators.ID, 'username')
    password = Element(Locators.ID, 'password')
    login_button = Element(Locators.NAME, 'login-submit')

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
