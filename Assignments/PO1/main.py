# create a geoJson file that contains a fictitious route visiting the single most populated city in each state
#Only the continental US and DC, but not Alaska or Hawaii.
import json
import random

#colors points
def randColor():
  r = lambda: random.randint(0,255)
  return ('#%02X%02X%02X' % (r(),r(),r()))


def plotPoint(city,noMSymbol):
  #at minimum a feature should have a property
  feature = {
    "type" : "Feature",
    "properties" : {
      "marker-color":randColor(),
      "marker-symbol": noMSymbol
    },
    "geometry" : {
      "type": "Point",
      "coordinates": [0,0]
    }
  }
 
  
  #gets lat,long details from json file
  #any other info is stored as key value
  for key,val in city.items():
    if key == 'latitude':
      #store latitude as y coordinate
      feature['geometry']['coordinates'][1] = val
    elif key == 'longitude':
      #store longitute as x coordinate
      feature['geometry']['coordinates'][0] = val
    else:
      feature['properties'][key] = val

  return feature

def drawLine(city):
  feature = {
    "type": "Feature",
    "properties": {
      "color":randColor()
    },
    "geometry": {
      "type": "LineString",
      "coordinates": [ 
      ]
    }
  }

  for cities in city:
    feature['geometry']['coordinates'].append([city[cities]['longitude'], city[cities]['latitude']])


  return feature

# def sortCity(states):
#   # load the json
#   # fp = open("new.geojson")
#   # states = json.load(fp)["features"]
#   #  which cities have I used already
#   used = []

#   # stupid large number
#   minimum = 99999999

#   # outer loop
#   for j in range(len(states)):
#     # inner loop 
#     for i in range(len(states)):
#      # is this value the new minimum?
#       print(states[i])
#       if i != j and states[i]["geometry"]["coordinates"][0] < minimum:
#       # if so, save it AND its index
#         if not i in used:
#           minimum = states[i]["geometry"]["coordinates"][0]
#           current = i
#   # current minimum gets saved
#     if not current in used:
#       used.append(current)

#    # reset minimum value
#     minimum = 99999999

# # order in which cities should appear is here 
#   return(used)



#open json file and read the entire file
with open("cities.json", 'r') as f:
  data = json.load(f)


statesDict = {}


for newCity in data:
  if newCity["state"] != 'Hawaii' and newCity["state"] != 'Alaska': 
    if newCity["state"] not in statesDict:
      #create a new key as a state with empty list
      statesDict[newCity["state"]] = []
    # append cities with similar state
    statesDict[newCity["state"]].append(newCity)

# print(statesDict)

# print("\n\n")

#set the max population to 0
maxPop = 0
maxCityPop = {}
#checking the cities in the statesDict
for city in statesDict:
  maxPop = 0
  #iterating through the value 
  for statePop in statesDict[city]:
    #if the max population is less than the state population
    maxPop = max(maxPop, statePop['population'])
    #needs the city and the city details with highest population
    if statePop['population'] == maxPop:
      #stores the state and the city with highest population
      maxCityPop[city] = statePop
      
# print("maxpop", maxPop)

# print(maxCityPop)

# citySorted = sortCity(maxCityPop)

    


points = []
noMSymbol= 1
coordinates =[]



for states in maxCityPop:
  # print(maxCityPop[states])
  points.append(plotPoint(maxCityPop[states], noMSymbol))
  # points.append(drawLine(maxCityPop[states]))

  noMSymbol = noMSymbol + 1
  # coordinates.append(drawLine(maxCityPop[states]))
# print(sortCity(points))
points.append(drawLine(maxCityPop))


# print(points)

#writing a geojson file
with open("new.geojson", "w") as f:
  #converting the points to json
  json.dump(points,f,indent=4)
    