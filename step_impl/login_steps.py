from getgauge.python import step
from step_impl.hooks.hooks import Hooks

@step("When I navigated to Login Page")
def when_i_navigated_to_login_page():
    Hooks.login_page.visit()
    
@step('When I login as <user_name> using <password>')
def when_i_login_as_using(user_name, password):
    Hooks.login_page.login(user_name, password)

@step('Then login should be successful')
def then_login_successful():
    Hooks.login_page.is_login_successful()