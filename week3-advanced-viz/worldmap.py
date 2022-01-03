
import webbrowser
from branca import colormap
import folium

class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
        self.my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)

    def showMap(self):
        #Display the map
        self.my_map.save("map.html")
        webbrowser.open("map.html")

    def addCity(self, cityname, coords):        
        city = folium.FeatureGroup()
        city.add_child(
            folium.CircleMarker(coords, radius=3, color = 'red')
        )
        folium.Marker(coords,popup=cityname).add_to(self.my_map)
    def addMarker(self, coords):
        folium.Marker(coords).add_to(self.my_map)
        

#Define coordinates of where we want to center our map
marker_coords = [51.5074, 0.1278] # London UK
coords = (34.852619, -82.394012) 

map = Map(center = coords, zoom_start = 2)

map.addCity(cityname='Greenville', coords = coords)

map.addMarker(marker_coords)

map.showMap()