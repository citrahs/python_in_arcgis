#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Citra
#
# Created:     03/09/2019
# Copyright:   (c) Citra 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

arcpy.env.overwriteOutput = True

baseURL = "(link_feature_service)/(id_number_feature_service)/query"
where = "1=1"
fields = "(field_feature_service)"

query = "?where={}&outFields={}&returnGeometry=true&f=json".format(where, fields)

fsURL = baseURL + query

fs = arcpy.FeatureSet()
fs.load(fsURL)

arcpy.CopyFeatures_management(fs, "(path_to_gdb)/(data_name)")

print("selesai")