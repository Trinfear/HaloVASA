import pandas as pd

skulls = pd.read_csv("skulls.csv", skiprows=0)
print(skulls.head())