import csv
import pandas as pd
import numpy as np
import scipy as sc
from scipy import stats

df = pd.read_csv('SurveyDataMain2CSV.csv')
#print(df.columns)
col_list = ['How many people do you live with excluding yourself?', 'If married, how many kids do you have?','Do you have any kids below 5 years old?', 'AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent']
df2 = df[col_list]


#getting the outliers for row 11 and 98

dfoutlier = df.drop(df.index[[11,98,49]])
dfoutlier.to_csv("surveyOutlier.csv")
#df2.to_csv("surveyResultsTest.csv")

df = dfoutlier


dfA = pd.DataFrame(df, columns=['How many people do you live with excluding yourself?', 'If married, how many kids do you have?','Do you have any kids below 5 years old?', 'AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent'])

dfA1 = dfA.rename(index= str, columns={'How many people do you live with excluding yourself?':"LivingWithNumbers", "If married, how many kids do you have?":"NoOfKids", "Do you have any kids below 5 years old?":"NoOfKidsBelow5", "AVG Class registered": "AvgClassRegistered", 'Avg Class Completed':"AvgClassCompleted", "Avg Class Dropped":"AvgClassDropped", "Completion Percent":"CompletionPercent", "Drop Percent":"DropPercent"})
#print(df_part2)

#Dropping empty Values
dfA1=dfA1.fillna(0)
completionPecent = np.average(dfA1['CompletionPercent'])
overallDropPercent = np.average(dfA1['DropPercent'])
#print(completionPecent, overallDropPercent)
#dfA1['NoOfKids'].replace('', np.nan, inplace=True)
dfA1.dropna(subset=['NoOfKids'], inplace=True)
dfA1.dropna(subset=['CompletionPercent'], inplace=True)

#print (dfA1.columns)
#print(dfA1.index)

#Analysis Part I
#dfA1_a = dfA1[(dfA1["LivingWithNumbers"] != "1") | (dfA1["NoOfKids"] != "0" ) | (dfA1["NoOfKids"] != "1" ) ]
dfA1_a = dfA1[(dfA1["LivingWithNumbers"] != "0") ]
dfA1_a = dfA1_a[(dfA1_a["LivingWithNumbers"] != "1") ]
dfA1_a = dfA1_a[(dfA1_a["LivingWithNumbers"] != "2") ]
dfA1_a = dfA1_a[(dfA1_a["NoOfKids"] != "0")]
#print(dfA1_a.as_matrix)
dfA1_a.to_csv("surveyResultsTest.csv")

#print(dfA1_a["CompletionPercent"])
#dfA1_a.dropna(subset=['CompletionPercent'], inplace=True)
print(np.average(dfA1['CompletionPercent']))
print(np.average(dfA1['DropPercent']))
dfA1_a.to_csv("surveyResultsTest.csv")
print("sum == " , dfA1_a['CompletionPercent'].sum())
print("Length " , len(dfA1_a))
print("Completion percent with living family members >2 and with kids == " , dfA1_a['CompletionPercent'].sum()/len(dfA1_a))
print("Drop percent with living family members >2 and with kids == " , dfA1_a['DropPercent'].sum()/len(dfA1_a))
print("TTest completion ==", stats.ttest_ind(dfA1['CompletionPercent'],dfA1_a['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfA1['DropPercent'],dfA1_a['DropPercent']))




# dfCompletion = dfA1_a['CompletionPercent'].astype(float)
# dfLivingWithNumbers = dfA1_a['LivingWithNumbers'].astype(float)
# print("Df Completion" , dfCompletion)
# correlation = np.corrcoef(dfCompletion,dfLivingWithNumbers)
# # correlation = dfA1_a['CompletionPercent'].apply(lambda s: dfA1_a["LivingWithNumbers"].corrwith(s))
# print("correlation == " , correlation)


print("Adding factor Kids above 5")
dfA1_a = dfA1_a[(dfA1_a["NoOfKidsBelow5"] == "Yes")]
dfA1_a.to_csv("surveyResultsTest.csv")

print("sum == " , dfA1_a['CompletionPercent'].sum())
print("Length " , len(dfA1_a))
print("Completion percent with living family members >2 and with kids above 5 == " , dfA1_a['CompletionPercent'].sum()/len(dfA1_a))
print("Drop percent with living family members >2 and with kids above 5== " , dfA1_a['DropPercent'].sum()/len(dfA1_a))
print("TTest completion ==", stats.ttest_ind(dfA1['CompletionPercent'],dfA1_a['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfA1['DropPercent'],dfA1_a['DropPercent']))

#analysis Part 1 part B students with no kids and just living with their significant another
dfA1_b = dfA1[(dfA1["LivingWithNumbers"] != "<=5") ]
dfA1_b = dfA1_b[(dfA1_b["LivingWithNumbers"] != "5+") ]
dfA1_b = dfA1_b[(dfA1_b["LivingWithNumbers"] != "2") ]
dfA1_b = dfA1_b[(dfA1_b["NoOfKids"] == "0")]
dfA1_b.to_csv("surveyResultsTest.csv")

print("Analysis for no kids and just living with their significant another")
print("sum == " , dfA1_b['CompletionPercent'].sum())
print("Length " , len(dfA1_b))
print("Completion percent with living family members <=1 and with no kids == " , dfA1_b['CompletionPercent'].sum()/len(dfA1_b))
print("Drop percent with living family members <=2 and with no kids == " , dfA1_b['DropPercent'].sum()/len(dfA1_b))
print("TTest completion ==", stats.ttest_ind(dfA1['CompletionPercent'],dfA1_b['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfA1['DropPercent'],dfA1_b['DropPercent']))

#Part 2 analysis


col_list2 = ['How many hours on average do you work at your job?', 'On a scale of 1-10 how demanding is your job?','On a scale 1 to 10 how social are you?','How many times do you go out for social activities during the week?', 'AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent']
df2 = df[col_list]
df2.to_csv("surveyResultsTest.csv")


dfB = pd.DataFrame(df, columns=['How many hours on average do you work at your job?', 'On a scale of 1-10 how demanding is your job?','On a scale 1 to 10 how social are you?','How many times do you go out for social activities during the week?', 'AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent'])

dfB1 = dfB.rename(index= str, columns={'How many hours on average do you work at your job?':"AvgWorkHours", 'On a scale of 1-10 how demanding is your job?':"JobDemandingScale",'On a scale 1 to 10 how social are you?':"SocialScale",'How many times do you go out for social activities during the week?':"NoOfSocialOuting", "AVG Class registered": "AvgClassRegistered", 'Avg Class Completed':"AvgClassCompleted", "Avg Class Dropped":"AvgClassDropped", "Completion Percent":"CompletionPercent", "Drop Percent":"DropPercent"})


#Dropping empty Values
dfB1.dropna(subset=['JobDemandingScale'], inplace=True)
dfB1.dropna(subset=['DropPercent'], inplace=True)
dfB1.to_csv("surveyResultsTest.csv")


#Analysis Part II

#Completion and drop with work hours 40 and less than 40
#dfB1_a = dfB1[(dfB1["AvgWorkHours"] == "<40") | (dfB1["AvgWorkHours"] == "40") | (dfB1["AvgWorkHours"] == ">40 but <=45")]
dfB1_a = dfB1[(dfB1["AvgWorkHours"] == "<40") | (dfB1["AvgWorkHours"] == "40")]

dfB1_a.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_a['CompletionPercent'].sum())
print("Length " , len(dfB1_a))
print("Completion percent with normal work hours( 40 and <40) students == " , dfB1_a['CompletionPercent'].sum()/len(dfB1_a))
print("Drop percent for normal work hours students ( 40 and <40) == " , dfB1_a['DropPercent'].sum()/len(dfB1_a))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_a['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_a['DropPercent']))
#Completion and Drop for work hours 40 +
#dfB1_b = dfB1[(dfB1["AvgWorkHours"] != "<40") & (dfB1["AvgWorkHours"] != "40") & (dfB1["AvgWorkHours"] != ">40 but <=45")]

dfB1_b = dfB1[(dfB1["AvgWorkHours"] != "<40") & (dfB1["AvgWorkHours"] != "40")]
dfB1_b.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_b['CompletionPercent'].sum())
print("Length " , len(dfB1_b))
print("Completion percent with lot of work hours( 40 +) students == " , dfB1_b['CompletionPercent'].sum()/len(dfB1_b))
print("Drop percent for lot of work hours students ( 40 +) == " , dfB1_b['DropPercent'].sum()/len(dfB1_b))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_b['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_b['DropPercent']))

## analysis with the Job demanding scale
print("analysis with the Job demanding scale 0 - 5 ")
dfB1_c = dfB1[(dfB1["JobDemandingScale"] == 1.0) | (dfB1["JobDemandingScale"] == 2.0) | (dfB1["JobDemandingScale"] == 3.0) | (dfB1["JobDemandingScale"] == 4.0) | (dfB1["JobDemandingScale"] == 5.0) ]

dfB1_c.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_c['CompletionPercent'].sum())
print("Length " , len(dfB1_c))
print("Completion percent with Job Demanding Scale <=5 " , dfB1_c['CompletionPercent'].sum()/len(dfB1_c))
print("Drop percent with Job Demanding Scale <=5  " , dfB1_c['DropPercent'].sum()/len(dfB1_c))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_c['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_c['DropPercent']))


print("analysis with the Job demanding scale 6 - 8 ")
dfB1_d = dfB1[(dfB1["JobDemandingScale"] == 6.0) | (dfB1["JobDemandingScale"] == 7.0) | (dfB1["JobDemandingScale"] == 8.0) ]

dfB1_d.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_d['CompletionPercent'].sum())
print("Length " , len(dfB1_d))
print("Completion percent with Job Demanding Scale 6-8 " , dfB1_d['CompletionPercent'].sum()/len(dfB1_d))
print("Drop percent with Job Demanding Scale 6-8  " , dfB1_d['DropPercent'].sum()/len(dfB1_d))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_d['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_d['DropPercent']))


print("analysis with the Job demanding scale 9 - 10 ")
dfB1_e = dfB1[(dfB1["JobDemandingScale"] == 9.0) | (dfB1["JobDemandingScale"] == 10.0) ]

dfB1_e.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_e['CompletionPercent'].sum())
print("Length " , len(dfB1_e))
print("Completion percent with Job Demanding Scale 9 -10 " , dfB1_e['CompletionPercent'].sum()/len(dfB1_e))
print("Drop percent with Job Demanding Scale 9 -10  " , dfB1_e['DropPercent'].sum()/len(dfB1_e))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_b['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_b['DropPercent']))


## analysis with the Social scale
print("analysis with the Social scale 0 - 5 ")
dfB1_f = dfB1[(dfB1["SocialScale"] == 1) | (dfB1["SocialScale"] == 2) | (dfB1["SocialScale"] == 3) | (dfB1["SocialScale"] == 4) | (dfB1["SocialScale"] == 5) ]

dfB1_f.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_f['CompletionPercent'].sum())
print("Length " , len(dfB1_f))
print("Completion percent with Social Scale <=5 " , dfB1_f['CompletionPercent'].sum()/len(dfB1_f))
print("Drop percent with Social Scale <=5  " , dfB1_f['DropPercent'].sum()/len(dfB1_f))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_f['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_f['DropPercent']))


print("analysis with the Social scale 6 - 8 ")
dfB1_g = dfB1[(dfB1["SocialScale"] == 6) | (dfB1["SocialScale"] == 7) | (dfB1["SocialScale"] == 8) ]

dfB1_g.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_g['CompletionPercent'].sum())
print("Length " , len(dfB1_g))
print("Completion percent with Social Scale 6-8 " , dfB1_g['CompletionPercent'].sum()/len(dfB1_g))
print("Drop percent with Social Scale 6-8  " , dfB1_g['DropPercent'].sum()/len(dfB1_g))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_g['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_g['DropPercent']))


print("analysis with the Social scale 9 - 10 ")
dfB1_h = dfB1[(dfB1["SocialScale"] == 9) | (dfB1["SocialScale"] == 10) ]

dfB1_h.to_csv("surveyResultsTest.csv")
#dfB1_h.to_csv("surveyOutlier.csv")
print("sum == " , dfB1_h['CompletionPercent'].sum())
print("Length " , len(dfB1_h))
print("Completion percent with Social Scale 9 -10 " , dfB1_h['CompletionPercent'].sum()/len(dfB1_h))
print("Drop percent with Social Scale 9 -10  " , dfB1_h['DropPercent'].sum()/len(dfB1_h))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_h['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_h['DropPercent']))




## analysis with the Going out activity
print("Going out Activity")
print("analysis with the Going out activity : 0 and 1 ")
dfB1_i = dfB1[(dfB1["NoOfSocialOuting"] == "0") | (dfB1["NoOfSocialOuting"] == "1") ]
dfB1_i.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_i['CompletionPercent'].sum())
print("Length " , len(dfB1_i))
print("Completion percent with Going out activity 0 and 1 " , dfB1_i['CompletionPercent'].sum()/len(dfB1_i))
print("Drop percent with Going out activity 0 and 1  " , dfB1_i['DropPercent'].sum()/len(dfB1_i))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_i['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_i['DropPercent']))



print("analysis with the Going out activity greater or equals to 2 ")
dfB1_j = dfB1[(dfB1["NoOfSocialOuting"] == "2") | (dfB1["NoOfSocialOuting"] == "<=5") | (dfB1["NoOfSocialOuting"] == "5+") ]

dfB1_j.to_csv("surveyResultsTest.csv")

print("sum == " , dfB1_j['CompletionPercent'].sum())
print("Length " , len(dfB1_j))
print("Completion percent with Going out activity >=2 " , dfB1_j['CompletionPercent'].sum()/len(dfB1_j))
print("Drop percent with Going out activity >=2  " , dfB1_j['DropPercent'].sum()/len(dfB1_j))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],dfB1_j['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],dfB1_j['DropPercent']))

# Combination of the anaylysis Part II(a)
print("Combination of Going out activity : 0 and 1(i), the Social scale 0 - 5(f) with normal work hours( 40 and <40) students (a), Demanding Job Scale 0 -5 (c)")
print("This was an interesting results but our sample size was very less ")
s1 = pd.merge(dfB1_i, dfB1_f, how='inner' )
s2 = pd.merge(dfB1_a, dfB1_c, how='inner' )
s3 = pd.merge(s1, s2, how='inner' )
s3.to_csv("surveyResultsTest.csv")
s3.to_excel("surveyResultsValus.xlsx")
#print(s3.as_matrix())

print("sum == " , s3['CompletionPercent'].sum())
print("Length " , len(s3))
print("Completion percent for Combination of Going out activity : 0 and 1(i), the Social scale 0 - 5(f) with normal work hours( 40 and <40) students (a), Demanding Job Scale 0 -5 (c) " , s3['CompletionPercent'].sum()/len(s3))
print("Drop percent for Combination of Going out activity : 0 and 1(i), the Social scale 0 - 5(f) with normal work hours( 40 and <40) students (a), Demanding Job Scale 0 -5 (c)  " , s3['DropPercent'].sum()/len(s3))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],s3['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],s3['DropPercent']))

# Combination of the anaylysis Part II(b)
print("Combination of Going out activity : Going out activity greater or equals to 2(j), the Social scale 9 - 10(h) with normal work hours( 40 and <40) students (a), Job demanding scale 9 - 10 (e)")
print("This was an interesting results but our sample size was very less ")
s4 = pd.merge(dfB1_j, dfB1_h, how='inner' )
s5 = pd.merge(dfB1_e, dfB1_b, how='inner' )
s6 = pd.merge(s4, s5, how='inner' )
s6.to_csv("surveyResultsTest.csv")
s6.to_excel("surveyResultsValus.xlsx")
#print(s3.as_matrix())

print("sum == " , s6['CompletionPercent'].sum())
print("Length " , len(s6))
print("Completion percent for Combination of Going out activity : Going out activity greater or equals to 2(j), the Social scale 9 - 10(h) with above average working hours( 40+ hours) students (b), Job demanding scale 9 - 10 (e)"  , s6['CompletionPercent'].sum()/len(s3))
print("Drop percent for Combination of Going out activity : 0 and 1(i), the Social scale 0 - 5(f) with above average working hours( 40+ hours) students (b), Demanding Job Scale 0 -5 (c)  " , s6['DropPercent'].sum()/len(s6))
print("TTest completion ==", stats.ttest_ind(dfB1['CompletionPercent'],s6['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfB1['DropPercent'],s6['DropPercent']))


#Analysis Part III

#Part 3 analysis


col_list3 = ['What do you wish to ultimately accomplish when starting an online course? Check all that apply.','AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent']
df3 = df[col_list]
df3.to_csv("surveyResultsTest.csv")


dfC = pd.DataFrame(df, columns=['What do you wish to ultimately accomplish when starting an online course? Check all that apply.','AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent'])

dfC1 = dfC.rename(index= str, columns={'What do you wish to ultimately accomplish when starting an online course? Check all that apply.':"AccomplishReason", "AVG Class registered": "AvgClassRegistered", 'Avg Class Completed':"AvgClassCompleted", "Avg Class Dropped":"AvgClassDropped", "Completion Percent":"CompletionPercent", "Drop Percent":"DropPercent"})


#Dropping empty Values
dfC1.dropna(subset=['AccomplishReason'], inplace=True)
dfC1.dropna(subset=['DropPercent'], inplace=True)
dfC1.to_csv("surveyResultsTest.csv")

#Completion and New Job Reason

dfC1_a = dfC1[(dfC1["AccomplishReason"] == "New Job")]
dfC1_a.to_csv("surveyResultsTest.csv")

print("sum == " , dfC1_a['CompletionPercent'].sum())
print("Length " , len(dfC1_a))
print("Completion percent with New Job reason for class == " , dfC1_a['CompletionPercent'].sum()/len(dfC1_a))
print("Drop percent for lot of New Job Reason for class == " , dfC1_a['DropPercent'].sum()/len(dfC1_a))
print("TTest completion ==", stats.ttest_ind(dfC1['CompletionPercent'],dfC1_a['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfC1['DropPercent'],dfC1_a['DropPercent']))

#Completion and Gain a degree Reason

dfC1_b = dfC1[(dfC1["AccomplishReason"] == "Gain a degree")]
dfC1_b.to_csv("surveyResultsTest.csv")

print("sum == " , dfC1_b['CompletionPercent'].sum())
print("Length " , len(dfC1_b))
print("Completion percent with Gain a degree reason for class == " , dfC1_b['CompletionPercent'].sum()/len(dfC1_b))
print("Drop percent for lot of Gain a degree Reason for class == " , dfC1_b['DropPercent'].sum()/len(dfC1_b))
print("TTest completion ==", stats.ttest_ind(dfC1['CompletionPercent'],dfC1_b['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfC1['DropPercent'],dfC1_b['DropPercent']))

#Completion and Knowledge Reason

dfC1_c = dfC1[(dfC1["AccomplishReason"] == "Knowledge")]
dfC1_c.to_csv("surveyResultsTest.csv")

print("sum == " , dfC1_c['CompletionPercent'].sum())
print("Length " , len(dfC1_c))
print("Completion percent with Knowledge reason for class == " , dfC1_c['CompletionPercent'].sum()/len(dfC1_c))
print("Drop percent for lot of Knowledge Reason for class == " , dfC1_c['DropPercent'].sum()/len(dfC1_c))
print("TTest completion ==", stats.ttest_ind(dfC1['CompletionPercent'],dfC1_c['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfC1['DropPercent'],dfC1_c['DropPercent']))

# #Completion and Practical skills Reason
# # No Data to support the claim
# dfC1_d = dfC1[(dfC1["AccomplishReason"] == "Practical skills")]
# dfC1_d.to_csv("surveyResultsTest.csv")
#
# print("sum == " , dfC1_d['CompletionPercent'].sum())
# print("Length " , len(dfC1_d))
# print("Completion percent with Practical skills reason for class == " , dfC1_d['CompletionPercent'].sum()/len(dfC1_d))
# print("Drop percent for lot of Practical skills Reason for class == " , dfC1_d['DropPercent'].sum()/len(dfC1_d))


# #Completion and Mental Challenge Reason
# # # No Data to support the claim
# dfC1_e = dfC1[(dfC1["AccomplishReason"] == "Mental Challenge")]
# dfC1_e.to_csv("surveyResultsTest.csv")
#
# print("sum == " , dfC1_e['CompletionPercent'].sum())
# print("Length " , len(dfC1_e))
# print("Completion percent with Mental Challenge reason for class == " , dfC1_e['CompletionPercent'].sum()/len(dfC1_e))
# print("Drop percent for lot of Mental Challenge Reason for class == " , dfC1_e['DropPercent'].sum()/len(dfC1_e))


#Analysis Part III

#Part 3 analysis


col_list3 = ['What do you wish to ultimately accomplish when starting an online course? Check all that apply.','AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent']
df3 = df[col_list]
df3.to_csv("surveyResultsTest.csv")


dfC = pd.DataFrame(df, columns=['What do you wish to ultimately accomplish when starting an online course? Check all that apply.','AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent'])

dfC1 = dfC.rename(index= str, columns={'What do you wish to ultimately accomplish when starting an online course? Check all that apply.':"AccomplishReason", "AVG Class registered": "AvgClassRegistered", 'Avg Class Completed':"AvgClassCompleted", "Avg Class Dropped":"AvgClassDropped", "Completion Percent":"CompletionPercent", "Drop Percent":"DropPercent"})


#Dropping empty Values
dfC1.dropna(subset=['AccomplishReason'], inplace=True)
dfC1.dropna(subset=['DropPercent'], inplace=True)
dfC1.to_csv("surveyResultsTest.csv")

#Completion and New Job Reason

dfC1_a = dfC1[(dfC1["AccomplishReason"] == "New Job")]
dfC1_a.to_csv("surveyResultsTest.csv")

print("sum == " , dfC1_a['CompletionPercent'].sum())
print("Length " , len(dfC1_a))
print("Completion percent with New Job reason for class == " , dfC1_a['CompletionPercent'].sum()/len(dfC1_a))
print("Drop percent for lot of New Job Reason for class == " , dfC1_a['DropPercent'].sum()/len(dfC1_a))
print("TTest completion ==", stats.ttest_ind(dfC1['CompletionPercent'],dfC1_a['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfC1['DropPercent'],dfC1_a['DropPercent']))


#Completion and Gain a degree Reason

dfC1_b = dfC1[(dfC1["AccomplishReason"] == "Gain a degree")]
dfC1_b.to_csv("surveyResultsTest.csv")
#dfC1_b.to_csv("surveyOutlier.csv")


print("sum == " , dfC1_b['CompletionPercent'].sum())
print("Length " , len(dfC1_b))
print("Completion percent with Gain a degree reason for class == " , dfC1_b['CompletionPercent'].sum()/len(dfC1_b))
print("Drop percent for lot of Gain a degree Reason for class == " , dfC1_b['DropPercent'].sum()/len(dfC1_b))
print("TTest completion ==", stats.ttest_ind(dfC1['CompletionPercent'],dfC1_b['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfC1['DropPercent'],dfC1_b['DropPercent']))


#Completion and Knowledge Reason

dfC1_c = dfC1[(dfC1["AccomplishReason"] == "Knowledge")]
dfC1_c.to_csv("surveyResultsTest.csv")

print("sum == " , dfC1_c['CompletionPercent'].sum())
print("Length " , len(dfC1_c))
print("Completion percent with Knowledge reason for class == " , dfC1_c['CompletionPercent'].sum()/len(dfC1_c))
print("Drop percent for lot of Knowledge Reason for class == " , dfC1_c['DropPercent'].sum()/len(dfC1_c))
print("TTest completion ==", stats.ttest_ind(dfC1['CompletionPercent'],dfC1_c['CompletionPercent']))
print("TTest drop ==", stats.ttest_ind(dfC1['DropPercent'],dfC1_c['DropPercent']))


# #Completion and Practical skills Reason
# # No Data to support the claim
# dfC1_d = dfC1[(dfC1["AccomplishReason"] == "Practical skills")]
# dfC1_d.to_csv("surveyResultsTest.csv")
#
# print("sum == " , dfC1_d['CompletionPercent'].sum())
# print("Length " , len(dfC1_d))
# print("Completion percent with Practical skills reason for class == " , dfC1_d['CompletionPercent'].sum()/len(dfC1_d))
# print("Drop percent for lot of Practical skills Reason for class == " , dfC1_d['DropPercent'].sum()/len(dfC1_d))


# #Completion and Mental Challenge Reason
# # # No Data to support the claim
# dfC1_e = dfC1[(dfC1["AccomplishReason"] == "Mental Challenge")]
# dfC1_e.to_csv("surveyResultsTest.csv")
#
# print("sum == " , dfC1_e['CompletionPercent'].sum())
# print("Length " , len(dfC1_e))
# print("Completion percent with Mental Challenge reason for class == " , dfC1_e['CompletionPercent'].sum()/len(dfC1_e))
# print("Drop percent for lot of Mental Challenge Reason for class == " , dfC1_e['DropPercent'].sum()/len(dfC1_e))



print("Part V analysis")
#Analysis Part V

#Part 5 analysis


# col_list5 = ['How much of the online content do you watch or read for the courses that you completed?','How many exercises or assessments did you complete for the courses that you completed?','AVG Class registered','Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent']
# df5 = df[col_list]
# df5.to_csv("surveyResultsTest.csv")


dfE = pd.DataFrame(df, columns=['How much of the online content do you watch or read for the courses that you completed?','How many exercises or assessments did you complete for the courses that you completed?','AVG Class registered',\
             'Avg Class Completed', 'Avg Class Dropped', 'Completion Percent', 'Drop Percent'])

dfE1 = dfE.rename(index= str, columns={'How much of the online content do you watch or read for the courses that you completed?':"ContentReadWatchedCompletedCourse",'How many exercises or assessments did you complete for the courses that you completed?':"AssignmentCompletedForCompletedCourse", "AVG Class registered": "AvgClassRegistered", 'Avg Class Completed':"AvgClassCompleted", "Avg Class Dropped":"AvgClassDropped", "Completion Percent":"CompletionPercent", "Drop Percent":"DropPercent"})

dfE1.to_csv("surveyResultsTest.csv")

#Dropping empty Values
# dfC1.dropna(subset=['AccomplishReason'], inplace=True)
# dfC1.dropna(subset=['DropPercent'], inplace=True)
# dfC1.to_csv("surveyResultsTest.csv")
#
# #Completion and New Job Reason
#
# dfC1_a = dfC1[(dfC1["AccomplishReason"] == "New Job")]
# dfC1_a.to_csv("surveyResultsTest.csv")
#
# print("sum == " , dfC1_a['CompletionPercent'].sum())
# print("Length " , len(dfC1_a))
# print("Completion percent with New Job reason for class == " , dfC1_a['CompletionPercent'].sum()/len(dfC1_a))
# print("Drop percent for lot of New Job Reason for class == " , dfC1_a['DropPercent'].sum()/len(dfC1_a))
#
#
# #Completion and Gain a degree Reason
#
# dfC1_b = dfC1[(dfC1["AccomplishReason"] == "Gain a degree")]
# dfC1_b.to_csv("surveyResultsTest.csv")
#
# print("sum == " , dfC1_b['CompletionPercent'].sum())
# print("Length " , len(dfC1_b))
# print("Completion percent with Gain a degree reason for class == " , dfC1_b['CompletionPercent'].sum()/len(dfC1_b))
# print("Drop percent for lot of Gain a degree Reason for class == " , dfC1_b['DropPercent'].sum()/len(dfC1_b))
#
#
# #Completion and Knowledge Reason
#
# dfC1_c = dfC1[(dfC1["AccomplishReason"] == "Knowledge")]
# dfC1_c.to_csv("surveyResultsTest.csv")
#
# print("sum == " , dfC1_c['CompletionPercent'].sum())
# print("Length " , len(dfC1_c))
# print("Completion percent with Knowledge reason for class == " , dfC1_c['CompletionPercent'].sum()/len(dfC1_c))
# print("Drop percent for lot of Knowledge Reason for class == " , dfC1_c['DropPercent'].sum()/len(dfC1_c))
#
#
# # #Completion and Practical skills Reason
# # # No Data to support the claim
# # dfC1_d = dfC1[(dfC1["AccomplishReason"] == "Practical skills")]
# # dfC1_d.to_csv("surveyResultsTest.csv")
# #
# # print("sum == " , dfC1_d['CompletionPercent'].sum())
# # print("Length " , len(dfC1_d))
# # print("Completion percent with Practical skills reason for class == " , dfC1_d['CompletionPercent'].sum()/len(dfC1_d))
# # print("Drop percent for lot of Practical skills Reason for class == " , dfC1_d['DropPercent'].sum()/len(dfC1_d))
#
#
# # #Completion and Mental Challenge Reason
# # # # No Data to support the claim
# # dfC1_e = dfC1[(dfC1["AccomplishReason"] == "Mental Challenge")]
# # dfC1_e.to_csv("surveyResultsTest.csv")
# #
# # print("sum == " , dfC1_e['CompletionPercent'].sum())
# # print("Length " , len(dfC1_e))
# # print("Completion percent with Mental Challenge reason for class == " , dfC1_e['CompletionPercent'].sum()/len(dfC1_e))
# # print("Drop percent for lot of Mental Challenge Reason for class == " , dfC1_e['DropPercent'].sum()/len(dfC1_e))
#
