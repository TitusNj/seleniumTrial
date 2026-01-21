from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(10)
driver.quit()
