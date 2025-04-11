#DO NOT RUN unless getting new year schedule! May incorporate this into main program.

import json
import fastf1

storedSchedule = {}
schedule = fastf1.get_event_schedule(2025)#Gets object of whole 2025 season
for i in range(1,25): #runs through each event num (ignoring 0 as only testing.)
    event = schedule.get_event_by_round(i) #gets the event by its round number.
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
    storedSchedule[str(event["EventDate"])] = infoDict # stored so that the main dict keys are the grand prix dates. Other info is a dict for each event stored in the main dict.
    #today is a race day if today, tomorrow, or the day after, is a date in the main dict as FP1 will be 2 days before the grand prix date.

with open("f1Data/events.json", "w") as f:
    json.dump(storedSchedule, f) # store in events.json.

print(storedSchedule)