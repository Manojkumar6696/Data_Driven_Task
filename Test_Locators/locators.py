"""
This file contains all the different locators
"""

class Locators:
    username_locator = '//input[@name="username"]' # Xpath
    password_locator = '//input[@name="password"]' #  Xpath
    login_button_locator = '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]' #  Xpath
    drop_down_selector = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p'
    logout = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'