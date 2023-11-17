from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:8000/authentication/login")

# Valid login credentials
time.sleep(3)
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")  

username_input.send_keys("san.do@mail.com")
password_input.send_keys("Admin415")
time.sleep(3)

login_button = driver.find_element(By.ID, "createUser")
login_button.click()

time.sleep(3) 

logout_button = driver.find_element(By.CLASS_NAME, "logout")
logout_button.click()

time.sleep(3)

# Invalid login credentials
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")   

username_input.clear()
password_input.clear()

username_input.send_keys("kan.do@mail.com")
password_input.send_keys("admin415")

time.sleep(3)

login_button = driver.find_element(By.ID, "createUser")
login_button.click()

time.sleep(3)
driver.quit()
