import pandas as pd
import numpy as np
import os

melb_data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\data\\melb_data.csv', sep=',')
#print(melb_data)

#print(melb_data.loc[15, 'Price'])
#print(melb_data.loc[90, 'Date'])

#print(melb_data.loc[3521, 'Landsize']/melb_data.loc[1690, 'Landsize'])

melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
count_int = 0
for col in melb_data.columns:
    if melb_data[col].dtype == 'int64':
        count_int+=1
print(melb_data['Type'].value_counts(normalize=True))
print(melb_data['Propertycount'].max())
print(melb_data['Distance'].std())
print((melb_data['BuildingArea'].median()-melb_data['BuildingArea'].mean())/melb_data['BuildingArea'].mean())

df = pd.DataFrame({'0': [1, 2, 4, 2, 3, 2, 1, 5, 6]})
print(df['0'].mode())

print(melb_data['Bedroom'].mode())


print(melb_data[melb_data['Bathroom'] == 0].shape[0])
print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3000000)].shape[0])
print(melb_data[melb_data['BuildingArea'] == 0]['Price'].min())
print(melb_data[(melb_data['Price'] < 1000000) & ((melb_data['Rooms'] > 5)|(melb_data['YearBuilt'] > 2015))]['Price'].mean())
print(melb_data[(melb_data['Price'] < 3000000) & (melb_data['Type'] == 'h')]['Regionname'].mode())



student_data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + r'\data\students_performance.csv', sep=',',
                           converters={'test preparation course': lambda x: x == 'completed'})

print(student_data.info())

