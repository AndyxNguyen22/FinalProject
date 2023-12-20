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

#Displays the dataFrame with height and weight categories
print("DataFrame with Height and Weight Categories:")
print(df)

#Getting a subset of the DataFrame using a boolean for "Tall Males Only"
subset_tall_males = df[(df['Height_Category'] == 'Tall') & (df['Gender'] == 'Male')]

#Display the DataFrame with added columns and subset
print("\nDataFrame with Subset:")
print(df)
print("\nSubset of Tall Males:")
print(subset_tall_males)

#Calculates the average height and weight for each gender
average_height = df.groupby('Gender')['Height'].mean()
average_weight = df.groupby('Gender')['Weight'].mean()

#Display the results for Average Height
print("\nAverage Height:")
print(average_height)

#Display the results for Average Weight
print("\nAverage Weight:")
print(average_weight)