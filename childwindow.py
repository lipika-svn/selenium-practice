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
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened=driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window"== driver.find_element(By.TAG_NAME,"h3").text

#driver.find_element(By.CSS_SELECTOR,"div[class='example']")
#driver.find_element(By.CSS_SELECTOR,"h3")
#driver.find_element(By.XPATH,"//h3")
#print(driver.find_element(By.TAG_NAME,"h3").text)