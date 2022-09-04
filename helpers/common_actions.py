import time
import helpers.utils as helper
from set_up import Browser_initilize


def login(self, username, password):
    login_menu_xpath = helper.get_xpath(self, 'LOGIN_MENU')
    login_username_xpath = helper.get_xpath(self, 'USERNAME_TXT_FIELD')
    login_password_xpath = helper.get_xpath(self, 'PASSWORD_TXT_FIELD')
    login_button_xpath = helper.get_xpath(self, 'LOGIN_BTN')

    helper.wait_and_click(self, login_menu_xpath)
    helper.clear_and_send_keys(self, login_username_xpath, username)
    helper.clear_and_send_keys(self, login_password_xpath, password)
    helper.wait_and_click(self, login_button_xpath)

