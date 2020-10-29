# by e.kelly
# this script will calculate distances between point locations that have the same name

import arcpy
import pandas as pd
import numpy as np

#input shapefile that contains clusters of settlement point locations with duplicate names
in_table = r'\\data\toponyms_over500m.shp'

#specify location where the shapefile will be saved as excel table
out_xls = r'\\data\moz_plnames_distant_inp.xls'

specify location where the results will be saved
out_csv = r'\\data\moz_distances_calculated.csv'
out_csv1 = r'\\data\moz_dist_cleaned.csv'  #cleaned table

#specify search distance
search_distance = 0.2

###################################################################################

#RUNS SCRIPT that will work with the above specified input and output data


#reads data as dataframe
arcpy.TableToExcel_conversion(in_table, out_xls)

mydf = pd.read_excel(out_xls, sheet_name='Sheet1')


def haversine(lon1, lat1, lon2, lat2):
    # convert degrees to radians
    lon1 = np.deg2rad(lon1)
    lat1 = np.deg2rad(lat1)
    lon2 = np.deg2rad(lon2)
    lat2 = np.deg2rad(lat2)

    # formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r_e = 6371
    return c * r_e

#Code merge
# merge dataframe on settlement names
m = mydf.reset_index().merge(mydf.reset_index(), on='moz_names')
# Calculate Distance
m['distance'] = haversine(m.x_x, m.y_x, m.x_y, m.y_y)


#save the merged table
m.to_csv(out_csv, encoding='utf-8')  















