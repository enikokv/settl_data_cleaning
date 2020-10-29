#written by e.kelly
#this is a raw script; ongoing tests
#the script deletes leading and trailing with space, writes settlement names to upper case
#the script also marks duplicates within the admin unit you have selected
#before you run the script make spatial join. Join your admin unit (spatially) to the settlement point layer.
#if you join the settlement contours to the settlement names make sure that you clipped the settl. point layer and you work with the clipped points only.


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlsxwriter
import arcpy



# Set environment settings
#arcpy.env.workspace = "c:/data"
arcpy.env.workspace = r'data/settlements'


in_table = r'\\data\Join_geonames_sections.shp'
out_xls = r'\\data\sec_geonames.xls'
out_csv = r'\\data\sec_geonames.csv'


settl_name = 'Name1'   # will search in this field for duplicates
adm_unit = 'OBJECTID_2'  # will search within these administrative units for duplicates


# Execute TableToExcel
arcpy.TableToExcel_conversion(in_table, out_xls)
mydf = pd.read_excel(out_xls, sheet_name='Sheet1', encoding="ISO-8859-1")


mydf[settl_name] = mydf[settl_name].str.strip()  #strips leading and trailing space
mydf[settl_name] = mydf[settl_name].str.upper()   #writes selected field as upper case
print mydf.head()

#find duplicates and mark them. The duplicates will get the attribute "True".
mydf['duplicated'] = mydf.duplicated(subset=[adm_unit, settl_name],keep=False)

#export result as .csv; you can open it in ArcGIS and save as shapefile
mydf.to_csv(out_csv, encoding='utf-8')

