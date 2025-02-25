from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.amazon.de/dp/B0CFVXMTHC?th=1")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(f"Price: {price.text}")