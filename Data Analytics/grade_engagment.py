import csv
import pandas as pd 


df = pd.read_csv('grades.csv')
col_list = ['Email','Username','Grade']
df = df[col_list]
df2 = pd.read_csv('test.csv')
df2 = df2.join(df.set_index('Username'), on='username')
df2.to_csv("resources/grade_engagement_info.csv")



