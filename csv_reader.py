import numpy
import pandas as pd
import pickle
def read_csv(filename):
    x = []
    rawdata = pd.read_csv(filename)
    columns = rawdata.columns
    y = numpy.nan_to_num(numpy.array(rawdata[columns[2]]))
    x = numpy.nan_to_num(numpy.array(rawdata[columns[2:]]))
    return x,y

# print(read_csv('kc_house_data.csv'))