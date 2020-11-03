#feature class to hdfs

import arcpy
import pandas as pd
from hdfs import InsecureClient
import os

arcpy.env.workspace = r'C:\folder\data.gdb'

fc = r'Sample'

field_names = [f.name for f in arcpy.ListFields(fc)]

Vars = ['OBJECTID', 'Param1', 'Param2', 'Param3']
spatRef = arcpy.Describe(fc).spatialReference
data = arcpy.da.FeatureClassToNumPyArray(fc, ["SHAPE@X","SHAPE@Y"] + Vars )

df = pd.DataFrame(data)

client_hdfs = InsecureClient('http://127.0.0.1:50070')

with client_hdfs.write('/user/root/folder/data.csv', encoding = 'utf-8') as writer:
    df.to_csv(writer)



