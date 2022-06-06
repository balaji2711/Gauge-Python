from getgauge.python import step
from step_impl.hooks.hooks import Hooks

@step('On Login Page')
def navigate_to_login_page():
    Hooks.login_page.visit()
    
@step('Login as <user_name> using <password>')
def login_as(user_name, password):
    Hooks.login_page.login(user_name, password)

@step('Login should be successful')
def login_successful():
    Hooks.login_page.is_login_successful()