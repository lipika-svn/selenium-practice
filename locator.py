import  time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#//Chrome driver service
service_obj=Service("C:/WebDrivers/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

time.sleep(5)
driver.maximize_window()

#id,Xpath,CSSSelector,Classname, name, linktest
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
time.sleep(5)
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()
time.sleep(5)

#xpath =//tagname[@attribute='value']--->//input[@type='submit']
#css=tagname[attribute='Value'],#id,.classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Lipika")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1")
time.sleep(5)
#Static drop-down
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value()


driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
#assert "Success123" in message
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


