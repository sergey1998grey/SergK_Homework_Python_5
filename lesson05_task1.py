from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CLASS_NAME, "btn-primary").click()

time.sleep(3)

driver.quit()
