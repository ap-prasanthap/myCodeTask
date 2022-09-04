import allure

import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time


@allure.description("Verify the login functionality")
@allure.severity(allure.severity_level.CRITICAL)
class Test_login_functionality(Browser_initilize):

    @allure.description("Verify the page title to ensure that the user is redirected to the landing screen")
    def test_user_launched_into_the_landing_screen(self):
        actual_title = helper.get_page_title(self)
        time.sleep(5)
        assert "Taiga" in actual_title, "User is not redirected to the login screen"

    @allure.description("Verify the Login and Sign Up menus are displayed landing screen")
    def test_login_and_signup_menus_are_displayed(self):
        login_menu_xpath = helper.get_xpath(self, 'LOGIN_MENU')
        signup_menu_xpath = helper.get_xpath(self, 'SIGNUP_MENU')
        assert helper.is_element_displayed(self,login_menu_xpath), "Login menu is not displayed"
        assert helper.is_element_displayed(self, signup_menu_xpath), "Sign Up menu is not displayed"

    @allure.description("Verify the user is redirected to the login screen")
    def test_user_is_navigated_to_the_login_screen(self):
        actual_title = helper.get_page_title(self)
        assert "Taiga" in actual_title, "User is not redirected to the login screen"

    @allure.description("Verify the user is able to login by using the valid credentials")
    def test_user_logged_in_with_valid_credentials(self):
        username = helper.get_data_parameters(self, 'username')
        password = helper.get_data_parameters(self, 'password')
        commonmethods.login(self,username,password)

    @allure.description("Verify the page title to ensure that the user is redirected to the users profile screen")
    def test_user_redirects_to_the_profile_screen(self):
        profile_menu_xpath = helper.get_xpath(self, 'PROFILE_MENU')
        helper.wait_and_click(self,profile_menu_xpath)
        actual_title = helper.get_page_title(self)
        expected_title = "Prasanth A P (@Prasanth123)"
        assert actual_title == expected_title, "User is not redirected to the profile screen"







