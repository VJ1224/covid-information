import urllib.request, json

with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
    data = json.load(url)

def printStates():
    for state in data:
        print(state)

def printDistricts(state):
    for district in data[state]['districtData'].values():
        print(district)

def getAllConfirmed():
    sum = 0
    for state in data:
        for district in data[state]['districtData'].values():
            sum += district['confirmed']
    return sum

def getAllActive():
    sum = 0
    for state in data:
        for district in data[state]['districtData'].values():
            sum += district['active']
    return sum

def getAllDeaths():
    sum = 0
    for state in data:
        for district in data[state]['districtData'].values():
            sum += district['deceased']
    return sum

def getAllRecovered():
    sum = 0
    for state in data:
        for district in data[state]['districtData'].values():
            sum += district['recovered']
    return sum

def getConfirmed(state, district = ""):
    if (district != ""):
        return data[state]['districtData'][district]['confirmed']
    else:
        sum = 0
        for district in data[state]['districtData'].values():
            sum += district['confirmed']
        return sum

def getDeaths(state, district = ""):
    if (district != ""):
        return data[state]['districtData'][district]['deceased']
    else:
        sum = 0
        for district in data[state]['districtData'].values():
            sum += district['deceased']
        return sum

def getActive(state, district = ""):
    if (district != ""):
        return data[state]['districtData'][district]['active']
    else:
        sum = 0
        for district in data[state]['districtData'].values():
            sum += district['active']
        return sum

def getRecovered(state, district = ""):
    if (district != ""):
        return data[state]['districtData'][district]['recovered']
    else:
        sum = 0
        for district in data[state]['districtData'].values():
            sum += district['recovered']
        return sum

def isState(s):
    present = False
    for state in data:
        if (state == s):
            present = True
    return present

def isDistrict(s,d):
    present = False
    for district in data[s]['districtData']:
        if (district == d):
            present = True
    return present
