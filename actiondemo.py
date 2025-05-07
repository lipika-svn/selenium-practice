from selenium import webdriver
from selenium.webdriver import ActionChains
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
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# MOUSE HOOVER
action=ActionChains(driver)
#action.click_and_hold()#(Hod for a sometime)
#action.double_click()
#action.context_click()#Rightclick()
#action.drag_and_drop() # source and Targe
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
