
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class RequestPage:
    URL = "https://optoutccpa-devenv.bigdbm.com/"

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        self.get_current_url()

    def go_home(self):
        return self.driver.URL

"Initializam o variabila in driver care interactioneaza cu browserul"
opt_out = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
opt_out.get()
opt_out.maximize_window()