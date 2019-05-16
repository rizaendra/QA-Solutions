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
        cls.driver = webdriver.Chrome(
            "C:/Users/Angga Pandu/PycharmProjects/FirstSeleniumTest/driverlib/chromedriver.exe")
        cls.driver.implicitly_wait(100)
        cls.driver.maximize_window()

    def test_validate_order(self):
        driver = self.driver
        driver.get(FRONTPAGE)

        # Loginpage
        login = LoginPage(driver)
        # Login Credentials
        login.enter_username("performance_glitch_user")
        login.enter_password("secret_sauce")
        # Go To homepage
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
        # Go to shopping cart
        home.click_shop_cart()

        # Cartpage
        cart = CartPage(driver)
        # Verify items
        self.assertTrue(cart.verify_backpack_cart(), "Sauce Labs Backpack")
        self.assertTrue(cart.verify_bolts_cart(), "Sauce Labs Bolt T-Shirt")
        self.assertTrue(cart.verify_ones_cart(), "Sauce Labs Onesie")
        self.assertTrue(cart.verify_reds_cart(), "Test.allTheThings() T-Shirt (Red)")
        self.assertTrue(cart.verify_jacket_cart(), "Sauce Labs Fleece Jacket")
        self.assertTrue(cart.verify_light_cart(), "Sauce Labs Bike Light")
        # Go to checkout
        cart.click_checkout()

        # Checkoutpage
        chkout = CheckoutPage(driver)
        # User Credentials
        chkout.enter_first_name("John")
        chkout.enter_last_name("Wick")
        chkout.enter_postal_code("12345")
        # Go to Checkout Overview Page
        chkout.click_ctn()

        # Checkout Overview Page
        chkoutOverview = CheckoutOverviewPage(driver)
        # Verify subtotal, tax and total
        self.assertTrue(chkoutOverview.verify_subtotal_label(), "$129.94")
        self.assertTrue(chkoutOverview.verify_tax_label(), "$10.40")
        self.assertTrue(chkoutOverview.verify_total_label(), "$140.34")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed!!!")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Angga Pandu/PycharmProjects/FirstSeleniumTest/Reports'))
