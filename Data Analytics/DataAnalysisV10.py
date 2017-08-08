import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

address = 'resources/summaryGradeEngagementCopy.csv'
readfileCSV = pd.read_csv(address)
#print(readfileCSV)


#### DataAnalysis######

###Group By######
# I am grouping by the students to see the co-relation of the students
# who got good grades Vs how many videos they watched
# 1-0.9 = A,
# 0.9-0.8 = B,
# 0.8 - 0.7 = C,
# 0.7 - 0.6 = C,
# < 0.6  F


print("Grade A")
gradeABoolean = (readfileCSV['Grade'] >= 0.90)
#print(gradeABoolean)
gradeA = readfileCSV.loc[gradeABoolean]
print(gradeA)


print("Grade B")
gradeBBoolean = (readfileCSV['Grade'] >= 0.80) & (readfileCSV['Grade'] < 0.90)
#print(gradeBBoolean)
gradeB = readfileCSV.loc[gradeBBoolean]
print(gradeB)

print("Grade C")
gradeCBoolean = (readfileCSV['Grade'] >= 0.70) & (readfileCSV['Grade'] < 0.80)
#print(gradeCBoolean)
gradeC = readfileCSV.loc[gradeCBoolean]
print(gradeC)

print("Grade D")
gradeDBoolean = (readfileCSV['Grade'] >= 0.60) & (readfileCSV['Grade'] < 0.70)
#print(gradeDBoolean)
gradeD = readfileCSV.loc[gradeDBoolean]
print(gradeD)

print("Grade F")
gradeFBoolean = ((readfileCSV['Grade'] < 0.60))
#print(gradeFBoolean)
gradeF = readfileCSV.loc[gradeFBoolean]
print(gradeF)


## Now lets calculate the total discussions done by the students of different Grades
print("Grade A Stats")
dissA = gradeA['discussions'].sum(axis=0)
dissA_average = dissA/ len(gradeA)
print("Grade A students average discussions == " , dissA_average)
problemsA = gradeA['problems'].sum(axis=0)
problemsA_average = problemsA/ len(gradeA)
print("Grade A students average problems solved == " , problemsA_average)
videosA = gradeA['videos'].sum(axis=0)
videosA_average = videosA/ len(gradeA)
print("Grade A students watched average videos == " , videosA_average)


print("Average grade for A-Grade == ",gradeA['Grade'].sum(axis=0)/len(gradeA))
print("Standard deviation for A-Grade distribution == ",np.std(gradeA['Grade']) )
print("Average videos watched for A-Grade == ",gradeA['videos'].sum(axis=0)/len(gradeA))
print("Standard deviation for A-Grade videos watched == ",np.std(gradeA['videos']))
print("Average discussion posted by students for A-Grade == ",gradeA['discussions'].sum(axis=0)/len(gradeA))
print("Standard deviation for A-Grade discussion post == ",np.std(gradeA['discussions']))
print("Average problems solved for A-Grade == ",gradeA['problems'].sum(axis=0)/len(gradeA))
print("Standard deviation for A-Grade problems solved == ",np.std(gradeA['problems']) )

print("Grade B Stats")
dissB = gradeB['discussions'].sum(axis=0)
dissB_average = dissB/ len(gradeB)
print("Grade B students average discussions == " , dissB_average)
problemsB = gradeB['problems'].sum(axis=0)
problemsB_average = problemsB/ len(gradeB)
print("Grade B students average problems solved == " , problemsB_average)
videosB = gradeB['videos'].sum(axis=0)
videosB_average = videosB/ len(gradeB)
print("Grade B students watched average videos == " , videosB_average)

print("Average grade for B-Grade == ",gradeB['Grade'].sum(axis=0)/len(gradeB))
print("Standard deviation for B-Grade distribution == ",np.std(gradeB['Grade']) )
print("Average videos watched for B-Grade == ",gradeB['videos'].sum(axis=0)/len(gradeB))
print("Standard deviation for B-Grade videos watched == ",np.std(gradeB['videos']))
print("Average discussion posted by students for B-Grade == ",gradeB['discussions'].sum(axis=0)/len(gradeB))
print("Standard deviation for B-Grade discussion post == ",np.std(gradeB['discussions']))
print("Average problems solved for B-Grade == ",gradeB['problems'].sum(axis=0)/len(gradeB))
print("Standard deviation for B-Grade problems solved == ",np.std(gradeB['problems']) )


print("Grade C Stats")
dissC = gradeC['discussions'].sum(axis=0)
dissC_average = dissC/ len(gradeC)
print("Grade C students average discussions == " , dissC_average)
problemsC = gradeC['problems'].sum(axis=0)
problemsC_average = problemsC/ len(gradeC)
print("Grade C students average proClems solved == " , problemsC_average)
videosC = gradeC['videos'].sum(axis=0)
videosC_average = videosC/ len(gradeC)


print("Average grade for C-Grade == ",gradeC['Grade'].sum(axis=0)/len(gradeC))
print("Standard deviation for C-Grade distribution == ",np.std(gradeC['Grade']) )
print("Average videos watched for C-Grade == ",gradeC['videos'].sum(axis=0)/len(gradeC))
print("Standard deviation for C-Grade videos watched == ",np.std(gradeC['videos']))
print("Average discussion posted by students for C-Grade == ",gradeC['discussions'].sum(axis=0)/len(gradeC))
print("Standard deviation for C-Grade discussion post == ",np.std(gradeC['discussions']))
print("Average problems solved for C-Grade == ",gradeC['problems'].sum(axis=0)/len(gradeC))
print("Standard deviation for C-Grade problems solved == ",np.std(gradeC['problems']) )



print("Grade D Stats")
dissD = gradeD['discussions'].sum(axis=0)
dissD_average = dissD/ len(gradeD)
print("Grade D students average discussions == " , dissD_average)
problemsD = gradeD['problems'].sum(axis=0)
problemsD_average = problemsD/ len(gradeD)
print("Grade D students average problems solved == " , problemsD_average)
videosD = gradeD['videos'].sum(axis=0)
videosD_average = videosD/ len(gradeD)
print("Grade D students watched average videos == " , videosD_average)

print("Average grade for D-Grade == ",gradeD['Grade'].sum(axis=0)/len(gradeD))
print("Standard deviation for D-Grade distribution == ",np.std(gradeD['Grade']) )
print("Average videos watched for D-Grade == ",gradeD['videos'].sum(axis=0)/len(gradeD))
print("Standard deviation for D-Grade videos watched == ",np.std(gradeD['videos']))
print("Average discussion posted by students for D-Grade == ",gradeD['discussions'].sum(axis=0)/len(gradeD))
print("Standard deviation for D-Grade discussion post == ",np.std(gradeD['discussions']))
print("Average problems solved for D-Grade == ",gradeD['problems'].sum(axis=0)/len(gradeD))
print("Standard deviation for D-Grade problems solved == ",np.std(gradeD['problems']) )


print("Grade F Stats")
dissF = gradeF['discussions'].sum(axis=0)
dissF_average = dissF/ len(gradeF)
print("Grade F students average discussions == " , dissF_average)
problemsF = gradeF['problems'].sum(axis=0)
problemsF_average = problemsF/ len(gradeF)
print("Grade F students average problems solved == " , problemsF_average)
videosF = gradeF['videos'].sum(axis=0)
videosF_average = videosF/ len(gradeF)
print("Grade F students watched average videos == " , videosF_average)

print("Average grade for F-Grade == ",gradeF['Grade'].sum(axis=0)/len(gradeF))
print("Standard deviation for F-Grade distribution == ",np.std(gradeF['Grade']) )
print("Average videos watched for F-Grade == ",gradeF['videos'].sum(axis=0)/len(gradeF))
print("Standard deviation for F-Grade videos watched == ",np.std(gradeF['videos']))
print("Average discussion posted by students for F-Grade == ",gradeF['discussions'].sum(axis=0)/len(gradeF))
print("Standard deviation for F-Grade discussion post == ",np.std(gradeF['discussions']))
print("Average problems solved for F-Grade == ",gradeF['problems'].sum(axis=0)/len(gradeF))
print("Standard deviation for F-Grade problems solved == ",np.std(gradeF['problems']) )

#Plot for Discussion
grades= ('A', 'B', 'C', 'D', 'F')
grade_position = np.arange(len(grades))
score = [dissA_average, dissB_average, dissC_average, dissD_average, dissF_average]
plt.bar(grade_position, score, align='center', alpha=0.5)
plt.xticks(grade_position, grades)
plt.ylabel('Average Discussion')
plt.title('Disscussions Vs Grades ')
plt.show()

#Plot for problems Solved
scorePS = [problemsA_average, problemsB_average, problemsC_average, problemsD_average, problemsF_average]
plt.bar(grade_position, scorePS, align='center', alpha=0.5)
plt.xticks(grade_position, grades)
plt.ylabel('Problems Solved')
plt.title('Problems Solved Vs Grades ')
plt.show()

#Plot for videos watched
scoreVW = [videosA_average, videosB_average, videosC_average, videosD_average, videosF_average]
plt.bar(grade_position, scoreVW, align='center', alpha=0.5)
plt.xticks(grade_position, grades)
plt.ylabel('Average videos watched')
plt.title('Average videos watched Vs Grades ')
plt.show()


## Average Grade in class
print("Average for ALL Students")
gradeAll = (readfileCSV['Grade'])
gradeAllAvg = gradeAll.sum()/len(gradeAll)
print("Average grade for all the students == ", gradeAllAvg)
gradeAllStd = np.std(gradeAll)
print("Standard deviation for All Grade distribution == ", gradeAllStd)


dissAll = (readfileCSV['discussions'])
dissAllAvg = dissAll.sum()/len(dissAll)
print("Average Discussion for all the students == ", dissAllAvg)
dissAllStd = np.std(dissAll)
print("Standard deviation for All Discussion distribution == ", dissAllStd)


probAll = (readfileCSV['problems'])
probAllAvg = probAll.sum()/len(probAll)
print("Average Problems solved for all the students == ", probAllAvg)
probAllStd = np.std(probAll)
print("Standard deviation for problems solved distribution == ", probAllStd)


vidAll = (readfileCSV['videos'])
vidAllAvg = vidAll.sum()/len(vidAll)
print("Average videos watched for all the students == ", vidAllAvg)
vidAllStd = np.std(vidAll)
print("Standard deviation for all videos watched distribution == ", vidAllStd)
