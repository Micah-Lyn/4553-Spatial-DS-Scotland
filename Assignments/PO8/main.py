import geopandas as gpd
import json


def openFile(fName):
    with open(fName) as f:
        data = gpd.read_file(f)
    
    #converts geodataframe to geojson object
    jData = json.loads(data.to_json(drop_id = True))
    jData = jData["features"]
    
    # returns a list of json obects and a gdf
    return data, jData

if __name__ == "__main__":
    statesGDF, states = openFile("states.geojson")
    citiesGDF, cities = openFile("cities.geojson")

    
    colors = ["#53013F", "#66023C", "#70435B", "#81516B", "#796878",
        "#A689E1", "#A689E1", "#BCA7E8", "#D6CADD", "#F8F4FF"]



    # create geoseries
    cities_s = gpd.GeoSeries(citiesGDF['geometry'])

    
    #buffer created to prevent multipolygon in alaska from touching
    states_s = gpd.GeoSeries(statesGDF["geometry"].buffer(0))

    # LOOP THROUGH STATES GEO DATAFRAME
    # Gets the cities within polygon similar to that of P03
    for i in range(len(statesGDF)):

        poly = states_s[i]
        #query cities within a polygon
        within_poly = cities_s.within(poly)

        # cindex store all the cities within a polygon/state
        # ensure polygon in list of features (outfile) are the same as polygons to color
        #city to match state
        states[i]["properties"]["cIndex"] = []

        
        population = 0

        #CHECK TO SEE WHICH CITY IS IN A POLYGON AND 
        #ADDS INDEX TO CINDEX AND CALCULATES POPULATION FOR EACH STATE
        for j in range(len(within_poly)):
            if within_poly[j] == True:
                # index comes after column name in dataframes
                population += citiesGDF["population"][j]

                 # index comes before keys in list of dictionaries
                # this appends the index of each cities that is "within" a state polygon
                states[i]["properties"]["cIndex"].append(j)

        # converted pop to a regular int since it was int64 and is not serializable by json
        #STORE POPULATION
        states[i]["properties"]["population"] = int(population)

    # sort features using population to assign color easier
    feature_list = sorted(states, key=lambda i: (
        i["properties"]["population"]), reverse=True)


    #ASSIGN COLOR TO STATE AND ASSOCIATED CITY
    # used as an index
    j = 0
    for i in range(len(colors)):

        count = 0
        while j < len(feature_list):
        
            # Changes the color, opacity and line around country for polygons
            feature_list[j]["properties"]["fill"] = colors[i]
            feature_list[j]["properties"]["fill-opacity"] = 1
            feature_list[j]["properties"]["stroke-width"] = 1

            # Looking at the list of cities indexes for each feature to 
            # change color and append to the feature list
            if "cIndex" in feature_list[j]["properties"]:
                points = feature_list[j]["properties"]["cIndex"]
                for point in points:
                    cities[point]["properties"]["marker-color"] = colors[i]
                    cities[point]["properties"]["marker-size"] = "small"
                    feature_list.append(cities[point])

            if count == 5 and j < 49:
                j += 1
                break
            j += 1
            count += 1    

    with open("outfile.geojson", "w") as f:
        json.dump(feature_list, f, indent=2)