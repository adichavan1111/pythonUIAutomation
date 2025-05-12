from tokenize import String

from pageObjects.dashboardPage import DashboardPage
from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig


class TestLogin:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicatipassword()

    def test_dashboard_page(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        # Create an instance of the Login page object
        self.lp = Login(self.driver)

        # Perform login steps
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()

        self.da = DashboardPage(self.driver)
        self.da.item()
        self.driver.save_screenshot(".\\screenshot\\" + "test_login.png")
        self.da.addCartButton()
        self.driver.save_screenshot(".\\screenshot\\" + "test_login.png")
        removed_text = self.da.removeCartButton().text
        print(removed_text)
        assert removed_text == "Remove", "Remove cart button mismatch"
        self.driver.save_screenshot(".\\screenshot\\" + "test_login.png")




