# -*- coding: utf-8 -*-
'''

Calculate Centroids of all GeoJSON polygon, import into Pandas DataFrame,
export to CSV fpr Dymo

'''

from osgeo import ogr
import pandas as pd

with open('neighborhoods.json', 'r') as f:
    hoods = ogr.Open('neighborhoods.json')

layer = hoods.GetLayer(iLayer=0)

lat, lng, name = [], [], []

#Get Centroids for each Polygon
count = 0
while (count < layer.GetFeatureCount()):
    try:
        feat = layer.GetNextFeature()
        centroid = feat.geometry().Centroid().GetPoint()
    except:
        count += 1
        continue
    lat.append(centroid[1])
    lng.append(centroid[0])
    name.append(feat['NAME'].lower().title())
    count += 1

#Throw them into DataFrame, write to CSV
df = pd.DataFrame({'latitude': lat, 'longitude': lng}, index=name)
df.index.name = 'name'
df['font size'] = 10
df['font file'] = 'fonts/helvetica.ttf'
df['point size'] = 2
df.to_csv('dymo_input.csv')
