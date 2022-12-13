from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
import os
from flight import Flight
from flightDetail import FlightDetail
from subcriber import Subscriber
from e_syntex import Emailing
import DatabaseAccess as db

class WebScraper:

    def connect_to_chrome(sub_info):

        # email = sub_info[3]
        # name = sub_info[0]
        # dob = sub_info[2]
        # gender = sub_info[1]
        # departure = sub_info[4]
        # arrival = sub_info[5]
        # sdate = sub_info[6]
        # edate = sub_info[7]

        email = "mad@email.com"
        name = "Sam Smith"
        dob = "1960-08-19"
        gender = "M"
        departure = "BOS"
        arrival = "MIA"
        sdate = "2023-01-02"
        edate = "2023-02-02"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        flight = Flight(departure, arrival, sdate, edate)
        subcriber = Subscriber(email, name, dob, gender)
        flightDetail = FlightDetail([], [], [])
        to_location = flight.get_arrival()
        dept_date = flight.get_sdate()
        arr_date = flight.get_edate()
        url = 'https://www.kayak.com/flights/BOS-{to_location}/{dept_date}/{arr_date}?sort=bestflight_a'.format(
            to_location=to_location, dept_date=dept_date, arr_date = arr_date)
        driver.get(url)
        sleep(10)
        driver.find_element
        flight_rows = driver.find_elements(
            By.XPATH, '//div[@class="inner-grid keel-grid"]')
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

        flightDetail.set_price(list_prices)
        flightDetail.set_airline(list_airlines)
        print(flightDetail.get_price())
        print(flightDetail.get_airline())
        db.receiver(subcriber,flight,flightDetail)
        subcriber_info = db.retrieve()
        #sub_email = Emailing(subcriber_info)
        #sub_email.to_string()

