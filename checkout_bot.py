import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# disable the geo location prompt upon browser startup
geoDisabled = webdriver.FirefoxOptions()
geoDisabled.set_preference("geo.enabled", False)
browser = webdriver.Firefox(geoDisabled)

browser.get("https://www.bestbuy.com/site/asus-nvidia-geforce-rtx-3060-dual-overclock-12gb-gddr6-pci-express-4-0-graphics-card-black/6557544.p?skuId=6557544")
# add item to cart
add_to_cart = browser.find_element('xpath', "/html/body/div[5]/main/div[6]/div/div/div/div/div/div/div[7]/div[1]/div/div[15]/div[1]/div/div/div/div/div/button")
browser.execute_script("arguments[0].click();", add_to_cart)

# go to cart
WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div/div[3]/div/div[1]"))).click()

#select shipping instead of local pickup
WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[1]/div[1]/section[1]/div[5]/ul/li/section/div[2]/div[2]/div/form/div[2]/fieldset/div[2]/div[1]/div/div[1]/span"))).click()
time.sleep(1)

# click checkout button
checkout = browser.find_element('xpath', "/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button")
browser.execute_script("arguments[0].click();", checkout)
time.sleep(4)

# continue as guest instead of signing in
continue_as_guest = browser.find_element('xpath', "/html/body/div[1]/div/section/main/div[2]/div/div/div[4]/div/div[2]/button")
browser.execute_script("arguments[0].click();", continue_as_guest)
time.sleep(4)

# fill in customer information and click apply then keep user entered information instead of recommendation
browser.find_element('css selector', "div.v-m-bottom-ss:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys("What's")
browser.find_element('css selector', "#lastName").send_keys("Good")
browser.find_element('css selector', "#street").send_keys("12345 Whats Hadnin Ave.")
browser.find_element('css selector', "#city").send_keys("In Yo City")
browser.find_element('css selector', "#state").send_keys("CA")
browser.find_element('css selector', "#zipcode").send_keys("12345")
apply_info = browser.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[3]/div[1]/section/div[1]/div[2]/div/div/div[2]/button')
browser.execute_script('arguments[0].click()', apply_info)
time.sleep(2)
keep_address = browser.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/button[2]')
browser.execute_script('arguments[0].click()', keep_address)
time.sleep(3)
browser.find_element('css selector', "#user\.emailAddress").send_keys("checkout_bot@gmail.com")
browser.find_element('css selector', "#user\.phone").send_keys("7145555555")

# click contiue to payment
continue_to_payment = browser.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[3]/div[1]/section/div[3]/section/div/div/button')
browser.execute_script("arguments[0].click()", continue_to_payment)
time.sleep(4)

# enter credit card information
browser.find_element('css selector', '#cc-number').send_keys('5462139438459284')
browser.find_element('css selector', '#expirationDate').send_keys('10/28')
browser.find_element('css selector', '#cvv').send_keys('123')
