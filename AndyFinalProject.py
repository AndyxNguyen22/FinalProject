#Andy's Final Project

#Importing 
import numpy 
import pandas as pd

#Imports CSV File
Weight_Height = "weight-height.CSV"

#Data and reading CSV file
data = pd.read_csv
df = pd.read_csv(Weight_Height)

#Vectorized computation to categorize individuals
#Individuals are categorize into short, normal, and tall for height using bins.
#Individuals are categorize into light, normal, and heavy for weight using bins. 
df['Height_Category'] = pd.cut(df['Height'], bins=[0, 58, 65, float('inf')], labels=['Short', 'Normal', 'Tall'])
df['Weight_Category'] = pd.cut(df['Weight'], bins=[0, 110, 170, float('inf')], labels=['Light', 'Normal', 'Heavy'])
