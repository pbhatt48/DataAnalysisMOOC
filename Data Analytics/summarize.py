import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import numpy.polynomial.polynomial as poly
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm
import statsmodels.formula.api as smf





df = pd.read_csv('resources/grade_engagement_info.csv')
df=df.fillna(0)
users = df['username'].unique()
with open('resources/summary_grade_engagement.csv', 'wb') as cs:
	writer = csv.writer(cs)
	writer.writerow(['Username', 'Grade', 'discussions', 'problems', 'videos'])
	for i in users:
		df2 = df[df['username']==i]
		sumDiscussions = sum(df2['discussion_contributions'])
		numVideos = sum(df2['videos_viewed'])
		numProblems = sum(df2['problems_correct'])
		grade = np.mean(df2['Grade'])
		writer.writerow([i,grade,sumDiscussions,numProblems,numVideos])

#Grade vs Video regressions
df = pd.read_csv('resources/summary_grade_engagement.csv')
slope,inter,rvalue,pvalue,stderr = stats.linregress(df['videos'], df['Grade'])
z = poly.polyfit(df['videos'], df['Grade'], 2)
x_new = np.random.choice(df['videos'], 2200, replace=False)
x_new_sorted = np.sort(x_new)
X1 = PolynomialFeatures(2).fit_transform(df['videos'].reshape(-1,1))
X1 = np.array(X1)
fit2 = sm.GLS(df['Grade'],X1).fit()
print fit2.summary()
fit1 = sm.OLS(df['Grade'], df['videos']).fit()
print fit1.summary()

plt.plot(df['videos'], df['Grade'], 'o', color='#00FFFF')
plt.xlabel('Videos Watched')
plt.ylabel('Grade')
plt.title("Number of videos watched versus Grade")
plt.savefig('GradeVVideo1.png')
plt.close()
plt.plot(df['videos'], df['Grade'], 'o', color='#00FFFF')
plt.plot(x_new_sorted, fit1.predict(x_new_sorted))
X1_sorted = PolynomialFeatures(2).fit_transform(x_new_sorted.reshape(-1,1))
plt.plot(x_new_sorted,fit2.predict(X1_sorted), color='red')
plt.xlabel('Videos Watched')
plt.ylabel('Grade')
plt.title("Number of videos watched versus Grade")
plt.savefig('GradeVVideo2.png')
plt.close()


#problems
x_new = np.random.choice(df['problems'], 2200, replace=False)
x_new_sorted = np.sort(x_new)
logfit = sm.Logit(df['Grade'], df['problems']).fit()
print logfit.summary()
fit1 = sm.OLS(df['Grade'], df['problems']).fit()
print fit1.summary()
plt.plot(df['problems'], df['Grade'], 'co')
plt.xlabel('problems solved')
plt.ylabel('Grade')
plt.title("Problems solved versus Grade")
plt.savefig('GradeVProblems1.png')
plt.close()

plt.plot(df['problems'], df['Grade'], 'co')
plt.plot(x_new_sorted,fit1.predict(x_new_sorted), color='black')
plt.xlabel('problems solved')
plt.ylabel('Grade')
plt.title("Problems solved versus Grade")
plt.savefig('GradeVProblems2.png')
plt.close()

#discussions
df = df[df.discussions<50]
x_new = np.random.choice(df['discussions'], 2200, replace=False)
x_new_sorted = np.sort(x_new)
logfit = sm.Logit(df['Grade'], df['discussions']).fit()
print logfit.summary()
fit1 = sm.OLS(df['Grade'], df['discussions']).fit()
print fit1.summary()
plt.plot(df['discussions'], df['Grade'], 'co')
plt.xlabel('Discussion posts')
plt.ylabel('Grade')
plt.title("Number of Discussion Posts versus Grade")
plt.savefig('GradeVDiscussion1.png')
plt.close()
plt.plot(df['discussions'], df['Grade'], 'co')
plt.plot(x_new_sorted,logfit.predict(x_new_sorted), color="black")
plt.plot(x_new_sorted,fit1.predict(x_new_sorted), color='red')
plt.xlabel('Discussion posts')
plt.ylabel('Grade')
plt.title("Number of Discussion Posts versus Grade")
plt.savefig('GradeVDiscussion2.png')
plt.close()




