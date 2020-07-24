#by e.kelly

import pandas as pd

#path to input file
in_xls = r'\\dataserver1\BMGFGRID\analysis\your_input_folder\your_input_data.xls'
#path to result
out_csv = r'\\dataserver1\BMGFGRID\analysis\your_output_folder\your_output_file.csv'


#SCRIPT====================================================
#path to list of string to searach for
find_string = r'\\dataserver1\BMGFGRID\scripts\cleaning\find_strings.csv'


#read data as pandas dataframe
df = pd.read_excel(in_xls, sheet_name='Sheet1')
#read file that contains string
data = pd.read_csv(find_string)

#specify column where to search for strings
targets = list(data["find_strings"])

sr = df.names.apply(lambda sentence: any(word in sentence for word in targets))
df1 = sr.to_frame()
df1.insert(0, 'NEW', range(0, 0 + len(df1)))
df_merged=pd.merge(df, df1, left_index=True, right_index=True)


df_merged.to_csv(out_csv, encoding='utf-8')
