# sourced from GIS StackExchange
# http://gis.stackexchange.com/a/78986/15499

import arcpy

# Make Feature Layers
arcpy.MakeFeatureLayer_management("GRID_600SCALE", "polylyr")
arcpy.MakeFeatureLayer_management("VW_ADDRESS", "pntlyr")
# Set output environment coordinate system to WGS 84 for web
arcpy.env.outputCoordinateSystem = GCS_WGS_1984
# loop through the unique list of polygons
for x in range(1,150):
    # Select Polygon Layer
    arcpy.SelectLayerByAttribute_management("polylyr", "NEW_SELECTION", "ID = " + str(x))
    # Select Intersecting Points
    arcpy.SelectLayerByLocation_management("pntlyr","INTERSECT","polylyr", "#", "NEW_SELECTION")
    # Copy Selected points to new shapefile in C:\temp folder
    arcpy.CopyFeatures_management("pntlyr", "c:/temp/point_" + str(x) + ".shp")