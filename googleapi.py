
####first you have to install gmaps ,gmplot using pip command ####
#### You can get a csv file in the folder of restaurants ####


import pandas as pd
import gmaps
import gmplot
a=pd.read_csv("C:\\Users\\sanket sanglikar\\Downloads\\Restaurants1.csv")
gmaps.configure(api_key='AIzaSyDUu7koYtpHQ_8P8R66zfCNqLEFAOv6QBM')
marker_locations=[]
for i in range(len(a['latitude'])):
    marker_locations.append([(a['longitude'][i]),(a['latitude'][i])])
fig = gmaps.figure(map_type='ROADMAP')
markers = gmaps.marker_layer(marker_locations)
fig.add_layer(markers)
fig
