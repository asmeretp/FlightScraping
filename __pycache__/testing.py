from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
# for dynamic search
# we can use the data we gather from UI for input as to_location and departure date

to_location = 'MIA'
dept_date = '2023-01-26'
url = 'https://www.kayak.com/flights/BOS-{to_location}/{dept_date}/2023-02-26?sort=bestflight_a'.format(
    to_location=to_location, dept_date=dept_date)

driver.get(url)
sleep(10)
driver.find_element

flight_rows = driver.find_elements(
    By.XPATH, '//div[@class="inner-grid keel-grid"]')
# print(flight_rows)

list_prices = []
list_airlines = []
list_stops = []
origin_stime = []
origin_etim = []
dest_stime = []
origin_etime = []
for WebElement in flight_rows:
    elementHTML = WebElement.get_attribute('outerHTML')
    elementSoup = BeautifulSoup(elementHTML, 'html.parser')

    # price
    temp_price = elementSoup.find(
        "div", {"class": 'col-price result-column js-no-dtog'})
    price = temp_price.find("span", {"class": "price-text"})
    list_prices.append(price.text)

    # airlines names
    airlines = elementSoup.find(
        "div", {"class": "bottom"})
    list_airlines.append(airlines.text)

    # stops
    stops = elementSoup.find(
        "span", {"class": "stops-text"})
    list_stops.append(stops.text)

# see changes now
    # departure and arrival time time
    otime = elementSoup.find(
        "span", {"class": "depart-time base-time"})
    origin_stime.append(otime.text)


print(list_prices)
print(list_airlines)
print(list_stops)
print(otime)
