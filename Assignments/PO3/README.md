P03 - Voronoi - Real World Use Case
### Micah-Lyn Scotland
### Description:
This program creates a voronoi diagram over the US creating polygons around each of the 49 cities. The UFO's are loaded into a spatial tree (geopandas rtree). The rtree is queried getting the UFO sighting points that are contained within each polygon. Results are saved to a json file for future use.


### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [main.py](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/main.py)     | Solution file.                                             |
|   2   | [input-ufo](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/data/BetterUFOData.csv)           | Input- UFO Data.   
|   3   | [input-shpfile](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/data/us_border_shp/us_border.shp)           | Input- Shp File.                 |
|   4   | [input-cities](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/cities.geojson)           | Input - Cities.                     |
|   5   | [output-voronoi](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/voronoi1.png)           | Voronoi Diagram                  |
|   6   | [output-json_file](https://github.com/Micah-Lyn/4553-Spatial-DS-Scotland/blob/main/Assignments/PO3/cityResults.json)          | City Polygon Coordinates, UFO Coordinates within each city                    |
