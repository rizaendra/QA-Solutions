class CheckoutCompletedPage():

    def __init__(self, driver):
        self.driver = driver

        self.completed_msg_xpath = "//h2[@class='complete-header']"
        self.bm_menu_xpath = "//button[contains(text(),'Open Menu')]"
        self.logout_menu_xpath = "//a[@id='logout_sidebar_link']"

    def verify_complete_message(self):
        complete_message = self.driver.find_element_by_xpath(self.completed_msg_xpath).text

        return complete_message

    def click_bm(self):
        self.driver.find_element_by_xpath(self.bm_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_menu_xpath).click()