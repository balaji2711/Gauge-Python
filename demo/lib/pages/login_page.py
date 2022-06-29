from framework.actions.selenium_actions import SeleniumActions
from getgauge.python import Messages

class LoginPageObjects:    
    txtUsername = "user-name"
    txtPassword = "password"    
    btnLogin = "login-button"
    title = "//span[@class='title']"

class LoginPage(SeleniumActions):
    
    def visit(self):
        self.driver.get(self.URL)
        Messages.write_message("Navigated to URL successfully")
    
    def login(self, username, password):        
        self.type("ID", LoginPageObjects.txtUsername, username)
        self.type("ID", LoginPageObjects.txtPassword, password)
        Messages.write_message("Entered username and password")
        self.click("ID", LoginPageObjects.btnLogin)
        Messages.write_message("Clicked on login button")

    def is_login_successful(self):                  
        assert self.get("XPATH", LoginPageObjects.title) == "PRODUCTS", "Login is not successful"
        Messages.write_message("Login is successful")