
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MasonMartin13",
    port='3306',
    database="Ticketing"
)
mycursor = db.cursor()

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

email = "papi@yahoo.com"
name = "Jiggelo Johnson"
DOB = "1998-01-23"
Gender = "M"
Subs = [email,name,DOB,Gender]

mycursor.execute("INSERT INTO Subscriber (Email,Name,DOB,Gender) Values (%s,%s,%s,%s)",Subs)

email = email
Arrival = "NY"
Departure = "Boston"
Date = "2022-01-23"
Fli = [email,Arrival,Departure,Date]
mycursor.execute("INSERT INTO flight (Email,Arrival,Departure,Date) Values (%s,%s,%s,%s)",Fli)

#gets the previous foreign key
Fli_ID = mycursor.lastrowid
print(Fli_ID)
Airline = "AA"
Time = "7:45"
price = "9999"
FliD = [Fli_ID,Airline,Time,price]
mycursor.execute("INSERT INTO flightDetail (FlightID,Airline,Time,Price) Values (%s,%s,%s,%s)",FliD)

db.commit()



