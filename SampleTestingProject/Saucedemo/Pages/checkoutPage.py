class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

        self.first_name_xpath = "//input[@placeholder='First Name']"
        self.last_name_xpath = "//input[@placeholder='Last Name']"
        self.postal_code_xpath = "//input[@placeholder='Zip/Postal Code']"
        self.continue_btn_xpath = "//input[@class='btn_primary cart_button']"

    def enter_first_name(self, firstname):
        self.driver.find_element_by_xpath(self.first_name_xpath).clear()
        self.driver.find_element_by_xpath(self.first_name_xpath).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element_by_xpath(self.last_name_xpath).clear()
        self.driver.find_element_by_xpath(self.last_name_xpath).send_keys(lastname)

    def enter_postal_code(self, postalcode):
        self.driver.find_element_by_xpath(self.postal_code_xpath).clear()
        self.driver.find_element_by_xpath(self.postal_code_xpath).send_keys(postalcode)

    def click_ctn(self):
        self.driver.find_element_by_xpath(self.continue_btn_xpath).click()