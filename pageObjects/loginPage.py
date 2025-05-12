from selenium.webdriver.common.by import By


class Login:
    textBox_Username_id = "user-name"
    textBox_password = "password"
    button_login = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        username_field = self.driver.find_element(By.ID, self.textBox_Username_id)
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.driver.find_element(By.ID, self.textBox_password)
        password_field.clear()
        password_field.send_keys(password)

    def login(self):
        login_button = self.driver.find_element(By.ID, self.button_login)
        login_button.click()
