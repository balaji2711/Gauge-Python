from getgauge.python import before_suite, after_suite, before_spec, after_spec
from step_impl.pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os

execute = os.getenv('execute')
browserName = os.getenv('browserName')
os.environ['GH_TOKEN'] = os.getenv('ghToken')

class Hooks:
    driver = None
    login_page = None
    print(execute)

@before_spec
def open_browser():    
    if execute == "Ui":
        if browserName == "chrome":
            Hooks.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))        
        elif browserName == "firefox":
            Hooks.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browserName == "ie":        
            Hooks.driver = webdriver.Ie(service=Service(IEDriverManager().install()))
        else:
            print('Browser not yet implemented - ' + browserName)
            raise Exception('Browser not yet implemented - ' + browserName)    
        Hooks.driver.maximize_window()
        Hooks.driver.delete_all_cookies()
        Hooks.login_page = LoginPage(Hooks.driver)    

@after_spec
def quit_browser():
    if execute == "Ui":
        Hooks.driver.close()
        Hooks.driver.quit()