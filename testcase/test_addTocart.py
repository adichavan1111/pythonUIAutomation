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