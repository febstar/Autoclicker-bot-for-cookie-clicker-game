from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


time.sleep(6)


button = driver.find_element(
    By.ID,
    'cookie'
)


contents = driver.find_elements(
    By.CSS_SELECTOR,
    '#store div'
)

lists = []
lists_id = [item.get_attribute("id") for item in contents]
timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    button.click()


    #Every 5 seconds:

    if time.time() > timeout:
        content = driver.find_elements(
            By.CSS_SELECTOR,
            '#store b'
        )
        item_prices = []
        for price in content:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = lists_id[n]

        money_count = driver.find_element(
            By.ID,
            'money'
        ).text

        if "," in money_count:
            money_count = money_count.replace(",", "")

        cookie_count = int(money_count)

        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        print(to_purchase_id)

        driver.find_element(
            By.ID,
            to_purchase_id
        ).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(
            By.ID,
            "cps"
        ).text
        print(cookie_per_s)
        break
