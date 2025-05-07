import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#//Chrome driver service
service_obj=Service("C:/WebDrivers/chromedriver.exe")
#service_obj=Service("C:/WebDrivers/msedgedriver.exe")
#service_obj=Service("C:/WebDrivers/gecodriver.exe")

driver= webdriver.Chrome(service=service_obj)
#driver= webdriver.Edge(service=service_obj)
#driver= webdriver.Firefox(service=service_obj)
#driver= webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') =='option2':
        checkbox.click()
        #assert checkbox.is_selected()
        break

radiobuttons= driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()





