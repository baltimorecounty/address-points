# clips.py script
# originally by @cageyjames
# forked by @talllguy
# https://gist.github.com/talllguy/7705827

import arcpy
 
from arcpy import env
 
env.workspace = "c:/workspace"
 
# variables
in_features = "soils.shp"
 
clip_features = "study_boundary.shp"
 
out_feature_class = "c:/workspace/output/study_area_soils.shp"
 
xy_tolerance = ""
 
# Execute Clip
 
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)