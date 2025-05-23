import pandas as pd

df = pd.read_csv("Dataset/Dataset_Cyber_Security_Indexes.csv")

df = df.drop_duplicates()

df = df.dropna()

df.to_csv('Dataset/Dataset_Cyber_Security_Indexes.csv', index=False)

#python3 Data_Cleaning/Dataset_Cyber_Security_Indexes.py   