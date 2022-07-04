from getgauge.python import step
from demo.hooks.hooks import Hooks
from demo.lib.pages.login_page import LoginPage


login_page = LoginPage(None)

@step("When I navigated to Login Page")
def when_i_navigated_to_login_page():
    global login_page
    login_page = LoginPage(Hooks.getContext())
    login_page.visit()
    
@step('When I login as <user_name> using <password>')
def when_i_login_as_using(user_name, password):
    login_page.login(user_name, password)

@step('Then login should be successful')
def then_login_successful():
    login_page.is_login_successful()