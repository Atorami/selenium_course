import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://worldofwarcraft.blizzard.com/en-us/")

# url = driver.current_url
# print("Page url ", url)
# assert url == "https://worldofwarcraft.blizzard.com/en-us/", "Url Error"

# current_title = driver.title
# print("Page title ", current_title)
# assert current_title == "World or warcraft", "Incorrect title"


print(driver.page_source)

time.sleep(3)