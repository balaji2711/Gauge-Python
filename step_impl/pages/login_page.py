from selenium.webdriver.common.by import By
from step_impl.actions.selenium_actions import SeleniumActions
from selenium.common.exceptions import NoSuchElementException

class LoginPageObjects:    
    txtUsername = "user-name"
    txtPassword = "password"    
    btnLogin = "login-button"
    title = "//span[@class='title']"

class LoginPage(SeleniumActions):
    
    def visit(self):
        self.driver.get(self.URL)
    
    def login(self, username, password):        
        self.type("ID", LoginPageObjects.txtUsername, username)
        self.type("ID", LoginPageObjects.txtPassword, password)
        self.click("ID", LoginPageObjects.btnLogin)

    def is_login_successful(self):                  
        assert self.get("XPATH", LoginPageObjects.title) == "PRODUCTS"