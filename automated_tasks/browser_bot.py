import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# driver.get("https://www.python.org")

# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget  time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# events ={}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }

# print(events)
# driver.quit()

# driver.get("https://secure-retreat-92358.herokuapp.com")

# fname = driver.find_element(By.NAME, "fName")
# lname = driver.find_element(By.NAME, "lName")
# email = driver.find_element(By.NAME, "email")
# button = driver.find_element(By.XPATH, "/html/body/form/button")
# fname.send_keys("John")
# lname.send_keys("Doe")
# email.send_keys("john@doe.com")
# button.click()


driver.get("https://orteil.dashnet.org/experiments/cookie/")


timer = time.time() + 2
timeout = time.time() + 60*5   # 5 minutes from now



while True:
    driver.find_element(By.ID, "cookie").click()

    if time.time() > timer:

        money = driver.find_element(By.ID, "money").text
        store = {}
        store_items = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        affordable_items = {}

        for n in range(len(store_items) - 1):
            store[n] = {
                "item": store_items[n].text.split("-")[0].strip(),
                "price": store_items[n].text.split("-")[1].strip().replace(",", "")
            }

        if "," in money:
                    money_element = money.replace(",", "")

        money = int(money)

        for item in store:
            if int(store[item]["price"]) < money:
                if int(store[item+1]["price"]) < money*2:
                    continue
                else:
                    affordable_items[item] = store[item]
        try:
            driver.find_element(By.ID, "buy"+ store[max(affordable_items)]["item"]).click()
        except ValueError:
             continue
        timer = time.time() + 2

    if time.time() > timeout:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

driver.quit()