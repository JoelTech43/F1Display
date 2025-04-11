import requests
import fastf1
import json
import arrow
utc = arrow.utcnow()
print(utc.format("DD-MM-YYYY HH:mm:ss"))

# x = requests.get('https://api.jolpi.ca/ergast/f1/2025/constructorstandings/')
# #print(x.json())

# for i in x.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]:
#     print(f"{i["Constructor"]["name"]} - {i["points"]}")

# y = requests.get('https://api.jolpi.ca/ergast/f1/2025/driverstandings/')
# #print(y.json())
# print("\n")
# for i in y.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]:
#     print(f"{i["Driver"]["givenName"]} {i["Driver"]["familyName"]} - {i["points"]}")

#z = requests.get('https://api.openf1.org/v1/drivers?session_key=latest')
#print(z.json())

# /*today is an event day is today, tomorrow, or the day after is an EventDate*/
