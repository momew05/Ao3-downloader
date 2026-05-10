from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

def choosetype():
    filetype = input("What type of files you want to download? (for example: EPUB)\n")
    return filetype

def download(driver, url, filetype):
    
    download_folder = os.path.abspath("downloaded files")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    driver.get(url)
    wait = WebDriverWait(driver, 10)

    doublecheck = driver.find_elements(By.LINK_TEXT, "Yes, Continue")
    if doublecheck:
        doublecheck[0].click()

    wait.until(ec.presence_of_element_located((By.CLASS_NAME, "download"))).click()

    driver.find_element(By.LINK_TEXT, filetype.upper()).click()
    while any(filename.endswith(".crdownloaded") for filename in os.listdir(download_folder)):
        time.sleep(1)
