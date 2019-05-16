class CartPage():

    def __init__(self, driver):
        self.driver = driver

        self.backpack_label_xpath = "//div[contains(text(),'Sauce Labs Backpack')]"
        self.boltShirt_label_xpath = "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]"
        self.onesIe_label_xpath = "//div[contains(text(),'Sauce Labs Onesie')]"
        self.light_label_xpath = "//div[contains(text(),'Sauce Labs Bike Light')]"
        self.fleeJacks_label_xpath = "//div[contains(text(),'Sauce Labs Fleece Jacket')]"
        self.shirtRed_label_xpath = "//div[contains(text(),'Test.allTheThings() T-Shirt (Red)')]"
        self.checkout_btn_xpath = "//a[@class='btn_action checkout_button']"
        self.bm_menu_xpath = "//button[contains(text(),'Open Menu')]"
        self.logout_link_linkText = "Logout"

    def click_bm(self):
        self.driver.find_element_by_xpath(self.bm_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()

    def verify_backpack_cart(self):
        backpack = self.driver.find_element_by_xpath(self.backpack_label_xpath).text

        return backpack

    def verify_bolts_cart(self):
        bolts = self.driver.find_element_by_xpath(self.boltShirt_label_xpath).text

        return bolts

    def verify_ones_cart(self):
        ones = self.driver.find_element_by_xpath(self.onesIe_label_xpath).text

        return ones

    def verify_reds_cart(self):
        reds = self.driver.find_element_by_xpath(self.shirtRed_label_xpath).text

        return reds

    def verify_jacket_cart(self):
        jacket = self.driver.find_element_by_xpath(self.fleeJacks_label_xpath).text

        return jacket

    def verify_light_cart(self):
        light = self.driver.find_element_by_xpath(self.light_label_xpath).text

        return light

    def click_checkout(self):
        self.driver.find_element_by_xpath(self.checkout_btn_xpath).click()