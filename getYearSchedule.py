#DO NOT RUN unless getting new year schedule! May incorporate this into main program.

import json
import fastf1

storedSchedule = {}
schedule = fastf1.get_event_schedule(2025)#.get_event_by_round(1)["EventDate"]
for i in range(1,25):
    event = schedule.get_event_by_round(i)
    infoDict = {
        "RoundNumber":int(event["RoundNumber"]),
        "EventName":event["EventName"],
        "Location":event["Location"],
        "Country":event["Country"],
        "Session1DateUtc":str(event["Session1DateUtc"]),
        "Session2DateUtc":str(event["Session2DateUtc"]),
        "Session3DateUtc":str(event["Session3DateUtc"]),
        "Session4DateUtc":str(event["Session4DateUtc"]),
        "Session5DateUtc":str(event["Session5DateUtc"]),
        "EventFormat":event["EventFormat"]
        }
    storedSchedule[str(event["EventDate"])] = infoDict

with open("f1Data/events.json", "w") as f:
    json.dump(storedSchedule, f)

print(storedSchedule)