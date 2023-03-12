import pandas as pd

dataFile = "TownData.csv"

df = pd.DataFrame()
data = pd.read_csv("Town Demographics 2010-2020.csv")

towns = []
for town in data["Town"]:
    if town not in towns:
        towns.append(town)
        
df["Town"] = towns
df.to_csv(dataFile)