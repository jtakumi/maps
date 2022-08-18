import folium
import pandas as pd
import json
import io
from PIL import Image
from selenium import webdriver

#create map object
m = folium.Map(location=[35,139],zoom_start=4)

National_Diet = [35.675888,139.744858]

folium.Marker(National_Diet,popup="国会議事堂").add_to(m)

m.save('National Diet.html')