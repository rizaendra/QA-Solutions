

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.product_inv_xpath = "//div[@class='product_label']"
        self.backpack_btn_xpath = "//div//div[@class='inventory_list']//div[1]//div[3]//button[1]"
        self.boltShirt_btn_xpath = "//div//div[@class='inventory_list']//div[3]//div[3]//button[1]"
        self.onesIe_btn_xpath = "//div//div[@class='inventory_list']//div[5]//div[3]//button[1]"
        self.shirtRed_btn_xpath = "//div//div[@class='inventory_list']//div[6]//div[3]//button[1]"
        self.fleeJacks_btn_xpath = "//div//div[@class='inventory_list']//div[4]//div[3]//button[1]"
        self.light_btn_xpath = "//div//div[@class='inventory_list']//div[2]//div[3]//button[1]"
        self.shopping_cart_xpath = "//*[contains(@class,'svg-inline--fa fa-shopping-cart fa-w-18 fa-3x')]"
        self.bm_menu_xpath = "//button[contains(text(),'Open Menu')]"
        self.logout_link_linkText = "Logout"

    def click_bm(self):
        self.driver.find_element_by_xpath(self.bm_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()

    def click_add_backpack(self):
        self.driver.find_element_by_xpath(self.backpack_btn_xpath).click()

    def click_add_bolts(self):
        self.driver.find_element_by_xpath(self.boltShirt_btn_xpath).click()

    def click_add_oni(self):
        self.driver.find_element_by_xpath(self.onesIe_btn_xpath).click()

    def click_add_reds(self):
        self.driver.find_element_by_xpath(self.shirtRed_btn_xpath).click()

    def click_add_jackets(self):
        self.driver.find_element_by_xpath(self.fleeJacks_btn_xpath).click()

    def click_add_light(self):
        self.driver.find_element_by_xpath(self.light_btn_xpath).click()

    def click_shop_cart(self):
        self.driver.find_element_by_xpath(self.shopping_cart_xpath).click()
