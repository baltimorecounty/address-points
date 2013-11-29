import arcpy

arcpy.env.workspace = r'C:\Export\address'
rows = arcpy.SearchCursor('address')
for row in rows:
    feat = row.Shape
    arcpy.Clip_analysis('address', feat, 'address_' + str(row.getValue('NAME')), '')