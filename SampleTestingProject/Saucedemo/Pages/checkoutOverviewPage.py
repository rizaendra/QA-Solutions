class CheckoutOverviewPage():

    def __init__(self, driver):
        self.driver = driver

        self.subtotal_label_xpath = "//div[@class='summary_subtotal_label']"
        self.tax_label_xpath = "//div[@class='summary_tax_label']"
        self.total_label_xpath = "//div[@class='summary_total_label']"
        self.finish_btn_xpath = "//a[@class='btn_action cart_button']"

    def verify_subtotal_label(self):
        subtotal_label = self.driver.find_element_by_xpath(self.subtotal_label_xpath).text

        return subtotal_label

    def verify_tax_label(self):
        tax_label = self.driver.find_element_by_xpath(self.tax_label_xpath).text

        return tax_label

    def verify_total_label(self):
        total_label = self.driver.find_element_by_xpath(self.total_label_xpath).text

        return total_label

    def click_fns(self):
        self.driver.find_element_by_xpath(self.finish_btn_xpath).click()