import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# to create download folder

download_dir = os.path.join(os.getcwd(), 'downloads')
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

options = webdriver.ChromeOptions()

prefs = {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'plugins.always_open_pdf_externally': True,
}

options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://patents.google.com/")
time.sleep(3)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("stent")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

first_result = driver.find_element(By.CSS_SELECTOR, 'search-result-item a')
first_result.click()
time.sleep(5)

pdf_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Download PDF")
pdf_button.click()
time.sleep(8)

files = os.listdir(download_dir)

pdf_files = [file for file in files if file.endswith(".pdf")]

if pdf_files:
    print("PDF Download Complete:",pdf_files[0] )

else:
    print("No PDFs Found")


driver.quit()