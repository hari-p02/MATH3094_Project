import pandas as pd

dataFile = "TownData.csv"

df = pd.read_csv(dataFile)

df.pop("3")

df.to_csv(dataFile)