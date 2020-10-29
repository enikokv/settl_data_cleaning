#e.kelly

#the script deletes leading and trailing with space, transforms names to upper case
#the script also deletes duplicates within the admin unit you have selected
#before you run the script make spatial join. Spatially join your admin unit laye to the settlement point layer.
#if you join the settlement contours to the settlement names make sure that you previously clipped the settl. point layer and you work with the clipped points only.


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlsxwriter
import arcpy



# Set environment settings
arcpy.env.workspace = r'\\settlements'


in_table = r'\\data\geonames_in_settlc.shp'
out_xls = r'\\data\geonames.xls'
out_csv = r'\\data\geonames.csv'

settl_name = 'Name1'   # will search in this field for duplicates
adm_unit = 'FID_2'  # will search within these administrative units for duplicates


# Execute TableToExcel
arcpy.TableToExcel_conversion(in_table, out_xls)
mydf = pd.read_excel(out_xls, sheet_name='Sheet1', encoding="ISO-8859-1")


mydf[settl_name] = mydf[settl_name].str.strip()  #strips leading and trailing space
mydf[settl_name] = mydf[settl_name].str.upper()   #writes selected field as upper case
print mydf.head()

# dropping duplicte values in grouped data, keeps first by default
mydf_clean = mydf.drop_duplicates(subset=[adm_unit, settl_name], keep='first')

#export result as .csv; you can open it in ArcGIS and save as shapefile
mydf_clean.to_csv(out_csv, encoding='utf-8')








