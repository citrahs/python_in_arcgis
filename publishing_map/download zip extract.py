#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Citra
#
# Created:     14/10/2019
# Copyright:   (c) Citra 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
import zipfile

url_data = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/shapes/zips/VNP14IMGTDL_NRT_SouthEast_Asia_24h.zip"
request = urllib2.urlopen(url_data)

zip_path = "D:/esri/webinar/arcpy/download_data/VNP14IMGTDL_NRT_SouthEast_Asia_24h.zip"
output = open(zip_path, "wb")
output.write(request.read())
output.close()

data_path = "D:/esri/webinar/arcpy/extract_data"
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(data_path)



