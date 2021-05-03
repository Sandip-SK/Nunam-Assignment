# importing pandas library and aliasing it as pd

import pandas as pd

# Storing the excel files in pandas dataframe sheets and sheets2

sheets=pd.read_excel("data.xlsx",sheet_name=None)
sheets2=pd.read_excel("data_1.xlsx",sheet_name=None)



# Creating pandes dataframe for each type of data in the sheets
# df , df2 , df3 are temporary dataframes to store individua sheets

detail=pd.DataFrame()
detailVol=pd.DataFrame()
detailTemp=pd.DataFrame()


# Separating and Concatenating Data from first excel

for i in sheets.keys():
    if('Detail_67_' in i):
        df=sheets[i]
        detail = pd.concat([details, df])
    elif('DetailVol_67_' in i):
        df2=sheets[i]
        detailVol = pd.concat([detailVol, df2])
    elif('DetailTemp_67_' in i):
        df3=sheets[i]
        detailTemp= pd.concat([detailTemp, df3])

# Separating and Concatenating Data from second excel

for i in sheets2.keys():
    if('Detail_67_' in i):
        df=sheets2[i]
        detail = pd.concat([details, df])
    elif('DetailVol_67_' in i):
        df2=sheets2[i]
        detailVol = pd.concat([detailVol, df2])
    elif('DetailTemp_67_' in i):
        df3=sheets2[i]
        detailTemp= pd.concat([detailTemp, df3])
print(details.info())
print(detailVol.info())
print(detailTemp.info())


# Exporting the resultant dataframes to .csv

detail.to_csv('detail.csv')
detailVol.to_csv('detailVol.csv')
detailTemp.to_csv('detailTemp.csv')
