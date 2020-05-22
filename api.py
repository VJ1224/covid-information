import urllib.request, json

with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
    stateData = json.load(url)

with urllib.request.urlopen("https://api.covid19india.org/zones.json") as url:
    zoneData = json.load(url)

with urllib.request.urlopen("https://api.covid19india.org/state_test_data.json") as url:
    stateTestData = json.load(url)

def printStates():
    for state in stateData:
        print(state)

def printDistricts(state):
    for district in stateData[state]['districtData'].values():
        print(district)

def getAllConfirmed():
    sum = 0
    for state in stateData:
        for district in stateData[state]['districtData'].values():
            sum += district['confirmed']
    return sum

def getAllActive():
    sum = 0
    for state in stateData:
        for district in stateData[state]['districtData'].values():
            sum += district['active']
    return sum

def getAllDeaths():
    sum = 0
    for state in stateData:
        for district in stateData[state]['districtData'].values():
            sum += district['deceased']
    return sum

def getAllRecovered():
    sum = 0
    for state in stateData:
        for district in stateData[state]['districtData'].values():
            sum += district['recovered']
    return sum

def getConfirmed(state, district = ""):
    if (district != ""):
        return stateData[state]['districtData'][district]['confirmed']
    else:
        sum = 0
        for district in stateData[state]['districtData'].values():
            sum += district['confirmed']
        return sum

def getDeaths(state, district = ""):
    if (district != ""):
        return stateData[state]['districtData'][district]['deceased']
    else:
        sum = 0
        for district in stateData[state]['districtData'].values():
            sum += district['deceased']
        return sum

def getActive(state, district = ""):
    if (district != ""):
        return stateData[state]['districtData'][district]['active']
    else:
        sum = 0
        for district in stateData[state]['districtData'].values():
            sum += district['active']
        return sum

def getRecovered(state, district = ""):
    if (district != ""):
        return stateData[state]['districtData'][district]['recovered']
    else:
        sum = 0
        for district in stateData[state]['districtData'].values():
            sum += district['recovered']
        return sum

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

def getZone(d):
    for district in zoneData['zones']:
        if district['district'] == d:
            return district['zone']

def getTests(s):
    sum = 0
    for state in stateTestData['states_tested_data']:
        if state['state'] == s:
            try:
                sum += int(state['totaltested'])
            except:
                pass
    return sum
