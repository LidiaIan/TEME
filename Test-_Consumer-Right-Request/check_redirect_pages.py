import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from base_page import RequestPage

# Metoda de identificare linku-ri din pagine


links = opt_out.find_elements(by=By.TAG_NAME, value="a")
for link in links:
    print(f"{link.tag_name}: {link.text}")


privacy = opt_out.find_element(by=By.LINK_TEXT, value="Privacy")
privacy.click()
time.sleep(5)

opt_out.get('https://optoutccpa-devenv.bigdbm.com/')
opt_out.maximize_window()

optofsale = opt_out.find_element(by=By.LINK_TEXT, value="Opt Out of Sale")
optofsale.click()
time.sleep(5)

opt_out.get('https://optoutccpa-devenv.bigdbm.com/')
opt_out.maximize_window()

privacy_policy = opt_out.find_element(by=By.LINK_TEXT, value="Privacy Policy")
opt_out.execute_script("arguments[0].scrollIntoView();", privacy_policy)
time.sleep(1)
privacy_policy.click()
time.sleep(5)


