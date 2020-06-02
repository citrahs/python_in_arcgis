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
import os

dir = r"path_to_gdb"
gdb = "nama_gdb.gdb"
arcpy.env.workspace = dir + gdb
fc = "nama_feature_class"

arcpy.AddXY_management(fc)

Table = os.path.join(dir, gdb, "nama_table")
Excel = os.path.join(dir, "fc_with_coordinate.xls")

arcpy.TableToExcel_conversion(Table, Excel)

print("proses komplit!")


