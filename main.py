from flask import Flask, render_template
import requests

app = Flask(__name__)

def getChampionshipsStandings(): #requests all data and then returns needed data.
    #constructorStanding and driverStanding are the leaderboards,
    #driverData provides extra needed data like team colours.
    constructorStanding = requests.get('https://api.jolpi.ca/ergast/f1/2025/constructorstandings/').json()["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]
    driverStanding = requests.get('https://api.jolpi.ca/ergast/f1/2025/driverstandings/').json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    driverData = requests.get('https://api.openf1.org/v1/drivers?session_key=latest').json()

    constructorTable = []
    constructorTable.append(["Position", "Name", "Points"]) #adds header row to constructorTable
    for constructor in constructorStanding:
        name = constructor["Constructor"]["name"]
        if name.split(" ")[0] == "RB": #Renaming RB to Racing Bulls to match driverData
            name = "Racing Bulls"
        position = constructor["position"]
        points = constructor["points"]
        colour = "#FFFFFF" #Default if real colour couldn't be found.
        count = 0
        done = False
        while not done and count < len(driverData): #Use while so that can exit once colour has been found
            driver = driverData[count] # will select every driver from driverData until finds one from the current team.
            if name.split()[0] in driver["team_name"]: #Checks first word of current team's name is in the driverData driver's team name. For some reason Alpine didn't work otherwise.
                teamColour = "#" + driver["team_colour"]
                done = True #don't have to check more drivers as have found the team colour
            count += 1
        constructorTable.append([position, name, points, teamColour]) #adds all of the data as a row in the constructorTable list. teamColour won't be displayed, just used for row colour
    
    driverTable = []
    driverTable.append(["Position", "Number", "Name", "Points", "Wins","Constructor"]) #adds header row to driverTable
    for driver in driverStanding:
        name = f"{driver["Driver"]["givenName"]} {driver["Driver"]["familyName"]}"
        position = driver["position"]
        points = driver["points"]
        wins = driver["wins"]
        number = driver["Driver"]["permanentNumber"]
        constructor = driver["Constructors"][0]["name"]
        if name == "Max Verstappen":
            number = "1" #Max's permanent number is 33 but he is current world champion so gets number 1.
        code = driver["Driver"]["code"] #Eg VER for Verstappen.
        teamColour = "#FFFFFF" #default colour if driver's team colour can't be found.
        count = 0
        done = False
        while not done and count < len(driverData): #Use while so that can exit once colour found.
            selectedDriver = driverData[count]
            if code == selectedDriver["name_acronym"]: #check is the same driver by comparing the driver code/acronym (eg VER for Verstappen) - more unique than first name.
                teamColour = "#" + selectedDriver["team_colour"]
                done = True #don't have to check more driverData drivers as have found the one we need.
            count += 1
        driverTable.append([position,number,name,points,wins,constructor,teamColour]) #adds all of the data as a row in the driverTable list. teamColour only used for row colour, not displayed as text.
    return constructorTable, driverTable #returns both lists

def getdata(): #proof of concept that I can run a function whenever the webpage is loaded.
    constructorTable, driverTable = getChampionshipsStandings()
    constructorHeadings = constructorTable[0]
    constructorData = constructorTable[1:]
    driverHeadings = driverTable[0]
    driverData = driverTable[1:]
    return constructorHeadings, constructorData, driverHeadings, driverData

@app.route("/")
def table():
    constructorHeadings, constructorData, driverHeadings, driverData = getdata()
    timeout = 10000 #change timeout based on whether it is a session or not.
    return render_template("tables.html", constructorHeadings=constructorHeadings, constructorData=constructorData, driverHeadings=driverHeadings, driverData=driverData, timeout=timeout) #renders the html file, passing it the table headers and data, and telling how long before reload.

print("hi")
app.run()