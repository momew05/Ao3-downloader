from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def createdriver():

    options = Options()
    
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")

    prefs = {
        "download.default_directory": os.path.abspath("downloaded files"),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    return driver

def getpage(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    checks = ("tos_agree", "data_processing_agree", "accept_tos")

    for check in checks:
        checkbox = wait.until(
            EC.element_to_be_clickable((By.ID, check))
        )
        checkbox.click()

    html = driver.page_source
    return html