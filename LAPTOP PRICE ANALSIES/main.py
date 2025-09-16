import pandas as pd
#Load_data 
data = pd.read_csv(r'C:\Users\pc\Desktop\python\project\laptop_data.csv')
#finding no fo null values in data 
print(data.isnull().sum())