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
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_multiple_items(self):
        driver = self.driver
        driver.get(FRONTPAGE)

        # Login
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        # Homepage or Productpage
        home = HomePage(driver)
        # Multiple Items
        home.click_add_backpack()
        home.click_add_bolts()
        home.click_add_oni()
        home.click_add_reds()
        home.click_add_jackets()
        home.click_add_light()
        home.click_shop_cart()

        cart = CartPage(driver)
        # Verify items
        self.assertTrue(cart.verify_backpack_cart(), "Sauce Labs Backpack")
        self.assertTrue(cart.verify_bolts_cart(), "Sauce Labs Bolt T-Shirt")
        self.assertTrue(cart.verify_ones_cart(), "Sauce Labs Onesie")
        self.assertTrue(cart.verify_reds_cart(), "Test.allTheThings() T-Shirt (Red)")
        self.assertTrue(cart.verify_jacket_cart(), "Sauce Labs Fleece Jacket")
        self.assertTrue(cart.verify_light_cart(), "Sauce Labs Bike Light")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed!!!")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Angga Pandu/PycharmProjects/FirstSeleniumTest/Reports'))
