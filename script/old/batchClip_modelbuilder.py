# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# batchClip_modelbuilder.py
# Created on: 2013-11-29 09:54:29.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")


# Local variables:
v600ScaleGrid_shp = "C:\\Export\\address\\600ScaleGrid.shp"
address = "C:\\Export\\address"
address_shp = "C:\\Export\\address\\600ScaleGrid.shp"
address_clip_shp = "C:\\Export\\address\\clip\\address_clip.shp"

# Process: Iterate Feature Classes
arcpy.IterateFeatureClasses_mb(address, "", "POINT", "NOT_RECURSIVE")

# Process: Clip
arcpy.Clip_analysis(address_shp, v600ScaleGrid_shp, address_clip_shp, "")
