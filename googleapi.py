
####first you have to install gmaps ,gmplot using pip command ####
#### You can get a csv file in the folder of restaurants ####


import gmaps
import pandas as pd
b=pd.read_csv("C:\\Users\\sanket sanglikar\\Downloads\\Restaurants1.csv")
gmaps.configure(api_key='AIzaSyDUu7koYtpHQ_8P8R66zfCNqLEFAOv6QBM')
marker=(b[["latitude","longitude"]])
fig1 = gmaps.figure()
markers1 = gmaps.marker_layer(marker)
fig1.add_layer(markers1)
fig1
