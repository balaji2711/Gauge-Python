from selenium.webdriver.common.by import By
from step_impl.actions.selenium_actions import SeleniumActions
from selenium.common.exceptions import NoSuchElementException

class LoginPageLocators:    
    txtUsername = (By.ID, "user-name")
    txtPassword = (By.ID, "password")
    btnLogin = (By.ID, "login-button")
    title = (By.XPATH, "//span[@class='title']")

class LoginPage(SeleniumActions):
    
    def visit(self):
        self.driver.get(self.URL)
    
    def login(self, username, password):   
        try:     
            self.set(LoginPageLocators.txtUsername, username)
            self.set(LoginPageLocators.txtPassword, password)
            self.click(LoginPageLocators.btnLogin)
        except NoSuchElementException as exception:
            print("Element not found and test failed - "+exception)

    def is_login_successful(self):        
        assert self.get(LoginPageLocators.title) == "PRODUCTS"