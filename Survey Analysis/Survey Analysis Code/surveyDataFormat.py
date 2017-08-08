import csv
import pandas as pd

df = pd.read_csv('../resources/Survey20Responses.csv')
col_list = ['6. How many people do you live with excluding yourself?', '7. If married, how many kids do you have?','8. Do you have any kids below 5 years old?', '15. How many online MOOC classes have you registered for so far?',\
            '16. Out of the MOOC classes that you have registered for, how many of them have you completed?', '17. Out of the MOOC classes that you have registered for, how many of them have you dropped?']
df = df[col_list]
df.to_csv("surveyResultsTest.csv")

print(df)
# df2 = pd.read_csv('profile.csv')
# df2=df2.drop('mailing_address', 1)
# df2=df2.drop('email', 1)
# df = df.join(df2.set_index('id'), on='Student ID')
# print df.ix[0]
# df.to_csv("grade_profile_info.csv")

#
# Students who are living with somebopfdy else
df2 = df.drop(df[df['6. How many people do you live with excluding yourself?'] == '0'].index)



# df2 = df.drop(df[df['6. How many people do you live with excluding yourself?'] != '<=5'].index and df[df['6. How many people do you live with excluding yourself?'] != '5+'].index)
# print(df2)

#Students who are living with their family members
df3 = df2.drop(df[df['6. How many people do you live with excluding yourself?'] == '1'].index)

#Students who have family and more than a kid

# removing NA kids
dfNAKids = df2.drop(df2[df2['7. If married, how many kids do you have?'].isnull()].index)
df4 = dfNAKids.drop(dfNAKids[dfNAKids['7. If married, how many kids do you have?'] == '0'].index)


#Students who have family and 2kids
df5 = df4.drop(df4[df4['7. If married, how many kids do you have?'] == '1'].index)

#Students who have family and more than 2kid
df6 = df5.drop(df5[df5['7. If married, how many kids do you have?'] == '2'].index)

df5.to_csv("surveyResultsValus.csv")

#print(df['6. How many people do you live with excluding yourself?'])



df = pd.read_csv('../resources/Survey20Responses.csv')
col2_list = ['10. How many hours on average do you work at your job?',"11. On a scale of 1-10, 1 how demanding is your job?", "12. On a scale 1 to 10, how social are you?","13. How many times do you go out for social activities during the week?", '16. Out of the MOOC classes that you have registered for, how many of them have you completed?', '17. Out of the MOOC classes that you have registered for, how many of them have you dropped?']
df_part2 = pd.DataFrame(df[col2_list])
df_part2.to_csv("surveyResultsTest.csv")

#get the rows
# df_part2.index = range(104)
# df_part2.to_csv("surveyResultsTest.csv")

#Reindex the columns
columns = ["", "AvgHours", "DemandScale", "SocialScale","GoOutTimes" "ClassCompleted", "ClassDropped"]
df_part2.columns = columns
df_part2.to_csv("surveyResultsTest.csv")

df_part2a = pd.DataFrame[df_part2["AvgHours"] != "40"]
print(df_part2a)
# df_part2a= df_part2.drop(df_part2[(df_part2["AvgHours"] != "40") and(df_part2["AvgHours"] != "<40")].index)
# df_part2a.to_csv("surveyResultsTest.csv")

# df_part2 = df_part2.rename(columns={'10. How many hours on average do you work at your job?':"AvgHours","11. On a scale of 1-10, 1 how demanding is your job?":"DemandScale", "12. On a scale 1 to 10, how social are you?":"SocialScale","13. How many times do you go out for social activities during the week?": "GoOutTimes", '16. Out of the MOOC classes that you have registered for, how many of them have you completed?':"ClassCompleted", '17. Out of the MOOC classes that you have registered for, how many of them have you dropped?':"ClassDropped"}, inplace=True)
#
# print(df_part2)
# df_part2.to_csv("surveyResultsTest.csv", sep='\t')


