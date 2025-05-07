
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#//Chrome driver service
service_obj=Service("C:/WebDrivers/chromedriver.exe")
#service_obj=Service("C:/WebDrivers/msedgedriver.exe")
#service_obj=Service("C:/WebDrivers/gecodriver.exe")
name='Lipika'
driver= webdriver.Chrome(service=service_obj)
#driver= webdriver.Edge(service=service_obj)
#driver= webdriver.Firefox(service=service_obj)
#driver= webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
alerttext=alert.text
print(alerttext)
assert name in alerttext
alert.accept()
#alert.dismiss()




