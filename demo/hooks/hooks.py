from getgauge.python import before_spec, after_spec, after_scenario, after_step
from demo.lib.pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from framework.utils.utils import Utils
from getgauge.python import Messages
from framework.actions.websocket_actions import WebsocketActions

execute = os.getenv('execute')
browserName = os.getenv('browserName')
headless = os.getenv('headless')

class Hooks:
    driver = None   

    def getContext():
        return Hooks.driver  

@before_spec
def open_browser():       
    if execute == "Ui": 
        if browserName == "chrome":
            chrome_options = Options()  
            if headless == "Yes":
                chrome_options.add_argument("--headless")
            Hooks.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=chrome_options)        
        elif browserName == "firefox":
            Hooks.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browserName == "ie":        
            Hooks.driver = webdriver.Ie(service=Service(IEDriverManager().install()))
        else:
            print('Browser not yet implemented - ' + browserName)
            raise Exception('Browser not yet implemented - ' + browserName)    
        Hooks.driver.maximize_window()
        Hooks.driver.delete_all_cookies()                    

@after_spec
def quit_browser(context):
    if execute == "Ui": 
        Hooks.driver.close()
        Hooks.driver.quit()
        print("Feature Name is - ", context._ExecutionContext__specification.name)

@after_step
def after_step(context):
    path = "\html-report\demo\\features\specs"
    print("Step Name is - ", context._ExecutionContext__step.text)
    print("Failing status is - ", context._ExecutionContext__step._Step__is_failing)
    if(context._ExecutionContext__step._Step__is_failing):     
        Messages.write_message("<img src='"+Utils.take_screenshot(Hooks.driver, path)+"' width='750' height='500'>")                   

@after_scenario
def quit_browser(context):
    print("Scenario Name is - ", context._ExecutionContext__scenario.name)
    print("Tag Name is - ", context._ExecutionContext__scenario.tags)
    print("Failing status is - ", context._ExecutionContext__scenario.is_failing)
    if WebsocketActions.is_open():
        WebsocketActions.close()
