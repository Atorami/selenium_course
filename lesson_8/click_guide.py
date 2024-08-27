import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.freeconferencecall.com/global/nl")

login_btn = driver.find_element("xpath", "//a[@id='login-desktop']")
login_btn.click()

email_filed = driver.find_element("xpath", "//input[@id='login_email']")
email_filed.send_keys("text@text.com")
time.sleep(3)
email_filed.clear()
time.sleep(3)
email_filed.send_keys("1111@text.com")
time.sleep(3)
# print(email_filed.get_attribute("value"))

