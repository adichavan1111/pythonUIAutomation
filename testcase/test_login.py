import time

from selenium.webdriver.common.by import By

from pageObjects.loginPage import Login
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class TestLogin:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicatipassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*****************Test home page title***********")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        print("Actual title:", act_title)

    # assert act_title == "nopCommerce demo store. Login", "Title"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        # Create an instance of the Login page object
        self.lp = Login(self.driver)

        # Perform login steps
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.logger.info("************Login successful***************")
        time.sleep(1)
        home_label = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        print("Actual title:", home_label)
        assert home_label == "Products", "Title mismatch"
        # assert self.driver.title == "Dashboard", "heading match"
        list_products = self.driver.find_elements(By.XPATH, "//*[@class='inventory_item']")
        count = len(list_products)
        print("Actual count:", count)
        assert count > 0, "Actual count mismatch"
        assert count == 6, "Actual count mismatch"
        firstItem_name = self.driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").text
        print("Actual firstItem name:", firstItem_name)
        assert firstItem_name == "Sauce Labs Backpack", "First Item name mismatch"
        self.driver.save_screenshot(".\\screenshot\\" + "test_login.png")
