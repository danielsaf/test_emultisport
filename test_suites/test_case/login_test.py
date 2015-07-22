__author__ = 'dsafinski'
# -*- coding: utf-8 -*-
import unittest
import test_suites
from test_suites.pages.login_page import LoginPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.login_page = test_suites.pages.login_page.LoginPage(self.driver, self.config['base_url'])

    def test_loginWithGoodCredential(self):
        self.login_page.login('ewa.baranowska@example.org', 'admin')
        assert 'Zalogowano jako: ewa.baranowska@example.org' in self.driver.page_source

    def test_loginWithWrongUsername(self):
        self.login_page.login('ewa.baranowska@example.orgtest', 'admin')
        # assert 'Nieprawidłowy e-mail lub hasło' in self.driver.page_source

    def test_loginWithWrongPassword(self):
        self.login_page.login('ewa.baranowska@example.org', 'test')
        # assert 'Nieprawidłowy e-mail lub hasło' in self.driver.page_source

    def test_loginWithNoCredential(self):
        self.login_page.login('', '')


if __name__ == "__main__":
    unittest.main()
