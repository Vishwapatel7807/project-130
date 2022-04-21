import pandas as pd
import csv

df = pd.read_csv('/Users/roshnipatel/Desktop/Projects(WhiteHat Jr)/project 130/total_stars.csv')
print(df.shape)

print(df.shape)
print(df.columns)
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
finaldata = df.dropna()
print(finaldata.head(5))
df.to_csv('main.csv')


