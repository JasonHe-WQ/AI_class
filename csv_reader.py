import numpy
import pandas as pd

def read_csv(filename):
    x = []
    rawdata = pd.read_csv(filename)
    columns = rawdata.columns
    y = numpy.array(rawdata[columns[2]])
    for i in columns[3:]:
        x.append(numpy.array(rawdata[i]))
    return x,y

