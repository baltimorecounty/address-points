# sourced from GIS StackExchange
# http://gis.stackexchange.com/a/78986/15499
# with a little help from ESRI
# http://resources.arcgis.com/en/help/main/10.1/index.html#//00170000006p000000

import arcpy
from arcpy import env

# Make Feature Layers
arcpy.MakeFeatureLayer_management("C:/Export/address/600ScaleGrid.shp", "polylyr")
arcpy.MakeFeatureLayer_management("C:/Export/address/address.shp", "pntlyr")

# loop through the unique list of polygons
for x in range(1,150):
    # Select Polygon Layer
    arcpy.SelectLayerByAttribute_management("polylyr", "NEW_SELECTION", "TAXMAP = " + str(x))
    # Select Intersecting Points
    arcpy.SelectLayerByLocation_management("pntlyr","INTERSECT","polylyr", "#", "NEW_SELECTION")
    # Copy Selected points to new shapefile in C:/Export folder
    arcpy.CopyFeatures_management("pntlyr", "C:/Export/address/clip/address_" + str(x) + ".shp")