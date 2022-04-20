P02 - Nearest Neighbor with UFO's
### Micah-Lyn Scotland
### Description:
This program loads data files into a geopandas geoseries spatial index. It calculates the distance from each city to every other city and store those values in either a csv or json file for use at a later time.A metric or threshold to "assign" a UFO sighting to a particular cit and the average distance to the 100 closest UFO's is calculated.


### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [main.py](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/main.py)     | Solution file.                                             |
|   2   | [input-ufo](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/data/BetterUFOData.csv)           | Input- UFO Data.   
|   3   | [input-shpfile](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/data/us_border_shp/us_border.shp)           | Input- Shp File.                 |
|   4   | [input-cities](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/cities.geojson)           | Input - Cities.                     |
|   5   | [output-voronoi](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/voronoi1.png)           | Voronoi Diagram                  |
|   6   | [output-json_file](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/cityResults.json)          | City Polygon Coordinates, UFO Coordinates within each city                    |
