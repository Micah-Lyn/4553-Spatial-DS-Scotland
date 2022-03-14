# %env MY_VAR=MY_VALUE
#find distances from each city to one another
#find the average distance 

# Load both data files (cities and UFO sightings)into a geopandas 
# geoseries spatial index.

#calculate distance from each city to every other city
#and store those values in either a csv or json file 

#determine a metric or threshold to assign a UFO sighting to
#a particular city. maybe the average distance to the 
# 100 closest UFO??? 




import json
import geopandas
from shapely.geometry import box, Polygon, LineString, Point
from csv import DictReader


#open files
with open("cities.geojson", 'r') as f:
  data = json.load(f)

#convert csv file into a dictionary
#where first row contains keys
#other rows r values...
#each line is a dictionary
ufos = []


with open('ufo_data.csv') as f:
  ufoSite = DictReader(f)

  for ufo in ufoSite:
    ufos.append(Point(float(ufo['lon']), float(ufo['lat'])))
    
  

gSeriesUfos = geopandas.GeoSeries(ufos)



points = []
city = []
state = []
#getting coordinates and storing it in points array
#create an array of arrays with points
for feature in data["features"]:
    if feature["geometry"]["type"] == "Point":
        points.append(feature["geometry"]["coordinates"])
        city.append(feature["properties"]["city"])

cities = []
for point in points:
    cities.append(Point(point))


#geoseries stores shapely geometric objects(points,curves etc)
#loading cities into geoseries
gSeriesCity = geopandas.GeoSeries(cities)

print(gSeriesCity)

#calculate distance from each city to every other city
#store it in a file for later use
#city, point, distances of other cites

cityDist1 =[]

for point in range(len(gSeriesCity)):

  cityDist=dict(gSeriesCity.distance(gSeriesCity[point]))

  #extracts the values and convert it to a list
  cityVals = list(cityDist.values())

  # print(cityVals)
  #hold the list of distances
  distance = []
  
  #converts the city and its values to a list 
  #so distances can be stores
  for i in range(len(cityVals)):
    distance.append({city[i]:cityVals[i]})

   
 #stores the city name and the distances of other cities
 #relative to that city
  citydistances = {'city':city[point],
    'coordinates': [gSeriesCity[point].x, gSeriesCity[point].y],
    'distance': distance
    }

  cityDist1.append(citydistances)



  

with open('citydistance.json', 'w') as w:
    w.write(json.dumps(cityDist1))


#determine a metric or threshold to assign a UFO sighting to
#a particular city. maybe the average distance to the 
# 100 closest UFO??? 

avgDist =[]
for point in range(len(gSeriesCity)):

  ufovals =dict(gSeriesUfos.distance(gSeriesCity[point]))
  #sort distances of ufo by values in dict
  ufovals1 = dict(sorted(ufovals.items(), key = lambda item: item[1]))

  #convert values of distances into a list to get average
  ufoValDistance = list(ufovals1.values())

  #get the first 100 distances from list
  length = 100
  ufoValDistance = ufoValDistance[:length]

  total = sum(ufoValDistance)
  #calculates the average distance of 100 closest ufos
  average = total/length


  #storing city, state, coordinates and average distance
  #of ufos
  citiesufo = {'city' : city[point],
    'coordinates': [gSeriesCity[point].x, gSeriesCity[point].y],
    'average distance': average
    }

  avgDist.append(citiesufo)

#writing the average ufo to a file
with open('cityaverageufo.json', 'w') as w:
    w.write(json.dumps(avgDist))

