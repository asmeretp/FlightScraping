import mysql.connector
from flightDetail import FlightDetail
from flight import Flight
from subcriber import Subscriber

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MasonMartin13",
    port='3306',
    database="Ticketing"
)
mycursor = db.cursor()


def Access_data():
    return 0


# mycursor.execute("DESCRIBE subscriber")
#
# for i in mycursor:
#     print(i)
# print("___________________________")
# mycursor.execute("DESCRIBE FlightDetail")
#
# for i in mycursor:
#     print(i)
# print("___________________________")
# mycursor.execute("DESCRIBE Flight")
#
# for i in mycursor:
#     print(i)

global email, name, DOB, Gender, Arrival, Departure, Date,Airline, time, price



def receiver(sub: Subscriber,fl: Flight, flD:FlightDetail):
    email = sub.get_email()
    name = sub.get_name()
    DOB = sub.get_dob()
    Gender = sub.get_gender()
    Subs = [email, name, DOB, Gender]
    mycursor.execute("INSERT INTO Subscriber (Email,Name,DOB,Gender) Values (%s,%s,%s,%s)", Subs)

    Arrival = fl.get_arrival()
    Departure = fl.get_departure()
    Date = fl.get_sdate()
    Fli = [email, Arrival, Departure, Date]
    mycursor.execute("INSERT INTO flight (Email,Arrival,Departure,Date) Values (%s,%s,%s,%s)", Fli)

    Fli_ID = mycursor.lastrowid
    print(Fli_ID)
    Airline = flD.get_airline()
    Time = flD.get_time()
    Price =  flD.get_price()
    FliD = [Fli_ID, Airline, Time, Price]
    mycursor.execute("INSERT INTO flightDetail (FlightID,Airline,Time,Price) Values (%s,%s,%s,%s)", FliD)
    db.commit()


def retrieve():
    script = "SELECT s.email,s.name,f.Departure, f.Arrival ,f.date,fd.Airline,fd.time,fd.Price FROM Ticketing.Subscriber s , Ticketing.Flight f ,Ticketing.FlightDetail fd where s.Email = f.Email and f.FlightID = fd.FlightID;"
    info=[]
    mycursor.execute(script)
    for i in mycursor:
         info.append(i)
    return info

