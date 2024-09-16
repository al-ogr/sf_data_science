import pandas as pd
import os

melb_data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\data\\melb_data.csv', sep=',')
print(melb_data)

print(melb_data.loc[15, 'Price'])
print(melb_data.loc[90, 'Date'])

print(melb_data.loc[3521, 'Landsize']/melb_data.loc[1690, 'Landsize'])