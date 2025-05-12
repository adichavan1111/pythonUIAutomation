from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
    first_Item_link = "item_4_title_link"
    add_cart_button ="//button[normalize-space()='Add to cart']"
    removed_text = "//button[normalize-space()='Remove']"

    def item(self):
        login_button = self.driver.find_element(By.ID, self.first_Item_link)
        login_button.click()

    def addCartButton(self):
        add_cart_button = self.driver.find_element(By.XPATH, self.add_cart_button)
        add_cart_button.click()
    def removeCartButton(self):
        removed_text = self.driver.find_element(By.XPATH, self.removed_text)
        return removed_text
