import  time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#//Chrome driver service
service_obj=Service("C:/WebDrivers/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

time.sleep(2)
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(5)
countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
print(len(countries))
time.sleep(5)
for country in countries:
    if country == "India":
        country.click()
        break

#print(driver.find_element(By.ID,"autosuggest").text)
assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=='India'




