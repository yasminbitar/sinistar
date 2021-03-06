from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

service = Service("C:\\Users\\yasmi\\Downloads\\chromedriver_windows\\chromedriver.exe")
options = Options()

options.binary_location = "C:\\Program Files\\Google\\Chrome Dev\\Application\\chrome.exe"

driver = webdriver.Chrome(chrome_options=options, service=service)

driver.get("https://staging.sinistar.ca/en/insured-request?step=login")

timeout = 5
try:
    element_present = EC.presence_of_element_located((By.NAME, 'firstName'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed Out")


#driver.find_element(By.NAME, 'firstName').send_keys('John')
#driver.find_element(By.NAME, 'lastName').send_keys('Smith')
#driver.find_element(By.NAME, 'email').send_keys('john.smith@hotmail.com')


#N = 1
driver.find_element(By.CSS_SELECTOR, "input[type='tel']").send_keys('(222) 222-2222')
#wb = driver.find_element(By.XPATH, "//input[@type='tel']");
#driver.execute_script("arguments[0].value='(222) 222-2222';", wb)
#wb.send_keys(Keys.TAB * N)
##driver.implicitly_wait(20)


#text_present = EC.text_to_be_present_in_element_value((By.XPATH, "//input[@type='tel']"), '(222) 222-2222')
#WebDriverWait(driver, timeout).until(text_present)

#driver.find_element(By.NAME, 'password').click()
#driver.find_element(By.NAME, 'password').send_keys('john123smith')
#driver.find_element(By.NAME, 'confirmation').click()
#driver.find_element(By.NAME, 'confirmation').send_keys('john123smith')


#submit = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[4]/form/button')
#driver.execute_script("Sign up", submit)

#driver.find_element(By.ID, 'Sign up').click()


#driver.close()


