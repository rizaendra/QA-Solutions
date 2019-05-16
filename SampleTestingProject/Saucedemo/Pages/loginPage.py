class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "user-name"
        self.password_textbox_id = "password"
        self.login_button_class = "btn_action"
        self.invalidUsernamePassword_msg_xpath = "//h3[@data-test='error']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_class_name(self.login_button_class).click()

    def verify_valid_username_message(self):
        #Epic sadface: Username and password do not match any user in this service
        valid_msg = self.driver.find_element_by_xpath(self.invalidUsernamePassword_msg_xpath).text

        return valid_msg

    def verify_invalid_username_message(self):
        #Epic sadface: Username and password do not match any user in this service
        invalid_msg = self.driver.find_element_by_xpath(self.invalidUsernamePassword_msg_xpath).text

        return invalid_msg

    def verify_locked_out_user(self):
        #Epic sadface: Sorry, this user has been locked out.
        lock_msg = self.driver.find_element_by_xpath(self.invalidUsernamePassword_msg_xpath).text

        return lock_msg