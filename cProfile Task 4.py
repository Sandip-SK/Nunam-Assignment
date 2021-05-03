import cProfile
import pandas as pd


def detailTemp_DS():
    # importing csv file as pandas dataframe
    dataframe = pd.read_csv('detailTemp.csv', parse_dates=["Realtime"], index_col="Realtime")
    # Downsampling to 1 minute Bins using resample('1T')
    dataframe = dataframe.resample('T').mean()
    # Exporting updated data to .csv file
    dataframe.to_csv('detailTempDownsampled.csv')


def detailVol_DS():
    # importing csv file as pandas dataframe
    dataframe = pd.read_csv('detailVol.csv', parse_dates=["Realtime"], index_col="Realtime")
    # Downsampling to 1 minute Bins using resample('1T')function
    dataframe = dataframe.resample('T').mean()
    # Exporting updated data to .csv file
    dataframe.to_csv('detailVolDownsampled.csv')


def detail_DS():
    dataframe = pd.read_csv('detail.csv', parse_dates=["Absolute Time"], index_col="Absolute Time")
    # Downsampling to 1 minute Bins using resample('1T')
    dataframe = dataframe.resample('T').mean()
    # Exporting updated data to .csv file
    dataframe.to_csv('detailDownsampled.csv')

# Applying cProfile 
cProfile.run('detailTemp_DS()')
cProfile.run('detailVol_DS()')
cProfile.run('detail_DS()')
