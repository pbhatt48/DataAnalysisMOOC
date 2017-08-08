import pandas as pd

df = pd.read_csv('grades.csv')
df = df[df.Grade > .10]
h=0
df = df.drop(df.index[0:175])
for i in df["Username"]:
	f = open('data/' + i + '.txt', 'rw')
	html = f.read()
	r = html.index("</body>")
	html = html[0:r]
	for j,df2 in enumerate(pd.read_html(html)):
		df2['username'] = i
		df2.to_csv("test.csv", index = False, mode='a', header=False)
	h+=1
	print h
