
from bs4 import BeautifulSoup
import requests

url = 'https://flights.booking.com/flights/BOS.AIRPORT-LHR.AIRPORT/?type=ROUNDTRIP&adults=1&cabinClass=ECONOMY&children=&from=BOS.AIRPORT&to=LHR.AIRPORT&fromCountry=US&toCountry=GB&fromLocationName=Logan+Airport&toLocationName=London+Heathrow+Airport&depart=2023-01-13&return=2023-01-21&sort=BEST&travelPurpose=leisure&aid=376370&label=booking-name-fByjJFqjmtwa1PGnD*I43QS541072772867%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9001982%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYnX0UuDUyu9mv9awMvJcBs'

result = requests.get(url)

soup = BeautifulSoup(result,'lxml')