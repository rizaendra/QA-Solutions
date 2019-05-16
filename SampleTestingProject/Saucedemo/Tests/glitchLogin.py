from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleTestingProject.Saucedemo.Pages.loginPage import LoginPage
from SampleTestingProject.Saucedemo.Pages.homePage import HomePage
from SampleTestingProject.Saucedemo.Pages.cartPage import CartPage
from SampleTestingProject.Saucedemo.Pages.checkoutPage import CheckoutPage
from SampleTestingProject.Saucedemo.Pages.checkoutOverviewPage import CheckoutOverviewPage
from SampleTestingProject.Saucedemo.Pages.checkoutCompleted import CheckoutCompletedPage
import HtmlTestRunner

FRONTPAGE = 'https://www.saucedemo.com/'

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Driver browser Chrome
        cls.driver = webdriver.Chrome("C:/Users/Angga Pandu/PycharmProjects/FirstSeleniumTest/driverlib/chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get(FRONTPAGE)

        # Login
        print("Try Login...")
        login = LoginPage(driver)
        login.enter_username("performance_glitch_user")
        login.enter_password("secret_sauce")
        login.click_login()
        # Homepage or Productpage
        home = HomePage(driver)
        #home.click_add_backpack()
        #Logout
        home.click_bm()
        home.click_logout()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed!!!")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Angga Pandu/PycharmProjects/FirstSeleniumTest/Reports'))
