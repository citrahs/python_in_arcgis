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

import arcpy
import os

arcpy.env.overwriteOutput = True

mxd = arcpy.mapping.MapDocument(r"D:/esri/webinar/arcpy/hotspot.mxd")

data_path = "D:/esri/webinar/arcpy/extract_data"

for df in arcpy.mapping.ListDataFrames(mxd):
    for layer in arcpy.mapping.ListLayers(mxd, "", df):
        arcpy.mapping.RemoveLayer(df, layer)
mxd.save()

filename = []

for file in os.listdir(data_path):
    if not file.endswith('.shp'):
        continue
    shp_file = os.path.join(data_path, file)
    filename.append(shp_file)


for i in filename:
    df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
    newLayer = arcpy.mapping.Layer(i)
    arcpy.mapping.AddLayer(df, newLayer, "BOTTOM")
mxd.save()

layerfile = "D:/esri/webinar/arcpy/symbolgy.lyr"
list_layer = arcpy.mapping.ListLayers(mxd)
for i in list_layer:
    arcpy.ApplySymbologyFromLayer_management(i, layerfile)
mxd.save()

file_path = "D:/esri/webinar/arcpy"
arcpy.mapping.ExportToPDF(mxd, file_path + "/output_map.pdf")

koneksi = file_path + "/arcgis on demo.esriindonesia.co.id (publisher).ags"

nama_service = "Hotspot"
sddraft = file_path + nama_service + '.sddraft'
sd = file_path + nama_service + '.sd'
summary = "peta hotspot 24 jam"
tags = 'hotspot'

arcpy.mapping.CreateMapSDDraft(mxd, sddraft, nama_service, 'ARCGIS_SERVER', koneksi, True, None, summary, tags)
analysis = arcpy.mapping.AnalyzeForSD(sddraft)
print(analysis)
arcpy.StageService_server(sddraft, sd)
arcpy.UploadServiceDefinition_server(sd, koneksi, in_public="PUBLIC")
print("Berhasil publish...")