import pandas as pd

dataFile = "TownData.csv"

newFile = "Town Drug Arrests 2010-2020"

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

# Read Collected Data Table to pandas Dataframe
df = pd.read_csv(dataFile,index_col="Index")

nd = pd.read_csv(newFile)
#print(nd)
new_column_name = "Drug Arrests per 10,000"

condition = "Age Range"          #Condition to be selected
select = "Total"             #What condition should be

measure_type = "Rate (per 10,000)"       # "Number" or "Percent"

variable = "Drug Arrests"         # Type of Data wanted

value = "Value"      # number wanted to be retrieved

#Add New Coloumn as Empty
df[new_column_name] = ''
for i in range(len(df)):   # for all towns
    sum = 0
    town = df.at[i, "Town"]             # (nd[condition] == select) & 
    for year in years:                  # for both sets of years
        row = nd.loc[(nd["Town"] == town) & (nd["Year"] == year) & (nd[condition] == select) &  (nd["Measure Type"] == measure_type) & (nd["Variable"] == variable)]
        
        val = row["Value"].values[0]
        sum += val
    
    average = round(sum/len(years),3)
    #print(str(town) + ": " + str(average))
    
    df.at[i, new_column_name] = average         #add to table


print(df)

# Update Collected Data Table file
df.to_csv(dataFile)