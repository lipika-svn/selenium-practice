import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#//Chrome driver service
service_obj=Service("C:/WebDrivers/chromedriver.exe")
#service_obj=Service("C:/WebDrivers/msedgedriver.exe")
#service_obj=Service("C:/WebDrivers/gecodriver.exe")

driver= webdriver.Chrome(service=service_obj)
#driver= webdriver.Edge(service=service_obj)
#driver= webdriver.Firefox(service=service_obj)



#driver= webdriver.Chrome()
driver.get("http://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)



time.sleep(20)