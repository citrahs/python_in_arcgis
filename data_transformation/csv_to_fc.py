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
arcpy.env.workspace = r"(path_to_gdb)/data.gdb"

input  = r"(path_to_csv)\data.csv"

output = "output_name"

lyr = arcpy.MakeXYEventLayer_management(input, 'longitude', 'latitude')
arcpy.FeatureClassToFeatureClass_conversion(lyr, arcpy.env.workspace, output)