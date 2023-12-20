#Andy's Final Project

#Importing 
import numpy 
import pandas as pd
import re

#Imports CSV File
Weight_Height = "weight-height.CSV"

#Data and reading CSV file (8.2)
data = pd.read_csv
df = pd.read_csv(Weight_Height)

#Vectorized computation to categorize individuals (8.1)
#Individuals are categorize into short, normal, and tall for height using bins.
#Individuals are categorize into light, normal, and heavy for weight using bins. 
df['Height_Category'] = pd.cut(df['Height'], bins=[0, 58, 65, float('inf')], labels=['Short', 'Normal', 'Tall'])
df['Weight_Category'] = pd.cut(df['Weight'], bins=[0, 110, 170, float('inf')], labels=['Light', 'Normal', 'Heavy'])

#Displays the dataFrame with height and weight categories
print("DataFrame with Height and Weight Categories:")
print(df)

#Getting a subset of the DataFrame using a boolean for "Tall Males Only" (8.3)
subset_tall_males = df[(df['Height_Category'] == 'Tall') & (df['Gender'] == 'Male')]

#Display the DataFrame with added columns and subset (8.3) (7.2)
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

#Display the results for Average Weight (7.2)
print("\nAverage Weight:")
print(average_weight)

#Search for a specific row based on user input (7.2)
print("\nSearch for a Specific Row by Row Number:")

#Allows the user to search for a row they want.
#The program then gives the user the information for the row they want.
while True:
    try:
        user_input = input("\nEnter the row number to search or type 'quit' to exit: ")
#Allows the user to quit the program if they type in "quit"
        if user_input.lower() == 'quit':
            print("Exiting the program. Thank you for using, goodbye!")
            break
        else:
#Takes user input (7.4)
#Uses a regular expression "re.match(r'^\d+$', user_input)" to make sure the number is an integer. 
            if re.match(r'^\d+$', user_input):
                row_number = int(user_input)
#Searches for row number
                search_result = df.iloc[[row_number]]
                if not search_result.empty:
#Displays the results for row number
                    print("\nSearch Result:")
                    print(search_result)
#Takes the results and adds it to a CSV file (8.4) (7.3)
                    search_result.to_csv(r'search_result.csv',index=False)
                    print("Search result printed to 'search_result.csv")
                else:
#If row number not found
                    print("\nRow not found.")
            else:
                print("\nInvalid input. Please enter avalid integer row number or type 'quit to exit. ")
#if user inputs a invalid input. User needs to enter an integer.
    except ValueError:
        print("Invalid input. Please enter a valid integer row number or type 'quit to exit.")
