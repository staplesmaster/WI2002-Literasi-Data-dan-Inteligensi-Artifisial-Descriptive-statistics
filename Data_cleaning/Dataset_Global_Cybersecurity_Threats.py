import pandas as pd

df = pd.read_csv("Dataset/Dataset_Global_Cybersecurity_Threats.csv")

df = df.drop_duplicates()

df = df.dropna()

df.to_csv('Dataset/Dataset_Global_Cybersecurity_Threats.csv', index=False)