import urllib.request, json

with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
    stateData = json.load(url)

with urllib.request.urlopen("https://api.covid19india.org/zones.json") as url:
    zoneData = json.load(url)

with urllib.request.urlopen("https://api.covid19india.org/state_test_data.json") as url:
    stateTestData = json.load(url)

with urllib.request.urlopen("https://api.covid19india.org/data.json") as url:
    nationalData = json.load(url)


def printStates():
    for state in stateData:
        print(state)

def printDistricts(state):
    for district in stateData[state]['districtData']:
        print(district)

def getAllConfirmed():
    return nationalData["statewise"][0]["confirmed"]

def getAllActive():
    return nationalData["statewise"][0]["active"]

def getAllDeaths():
    return nationalData["statewise"][0]["deaths"]

def getAllRecovered():
    return nationalData["statewise"][0]["recovered"]

def getTodayConfirmed():
    return nationalData["cases_time_series"][-1]["dailyconfirmed"]

def getTodayDeaths():
    return nationalData["cases_time_series"][-1]["dailydeceased"]

def getTodayRecovered():
    return nationalData["cases_time_series"][-1]["dailyrecovered"]

def getTodayDate():
    return nationalData["cases_time_series"][-1]["date"]

def getStateConfirmed(state):
    for i in range(len(nationalData["statewise"])):
        if state == nationalData["statewise"][i]["state"]:
            return nationalData["statewise"][i]["confirmed"]

def getStateDeaths(state):
    for i in range(len(nationalData["statewise"])):
        if state == nationalData["statewise"][i]["state"]:
            return nationalData["statewise"][i]["deaths"]

def getStateActive(state):
    for i in range(len(nationalData["statewise"])):
        if state == nationalData["statewise"][i]["state"]:
            return nationalData["statewise"][i]["active"]

def getStateRecovered(state):
    for i in range(len(nationalData["statewise"])):
        if state == nationalData["statewise"][i]["state"]:
            return nationalData["statewise"][i]["recovered"]

def getDistrictConfirmed(state, district):
    return stateData[state]['districtData'][district]['confirmed']

def getDistrictDeaths(state, district):
    return stateData[state]['districtData'][district]['deceased']

def getDistrictActive(state, district):
    return stateData[state]['districtData'][district]['active']

def getDistrictRecovered(state, district):
    return stateData[state]['districtData'][district]['recovered']

def isState(s):
    present = False
    for state in stateData:
        if (state == s):
            present = True
    return present

def isDistrict(s,d):
    present = False
    for district in stateData[s]['districtData']:
        if (district == d):
            present = True
    return present

def getDistrictZone(d):
    for district in zoneData['zones']:
        if district['district'] == d:
            return district['zone']

def getStateTests(s):
    data = []
    for state in stateTestData['states_tested_data']:
        if state['state'] == s:
            data.append(state)
    return data[-1]['totaltested']
