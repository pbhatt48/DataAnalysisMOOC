from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import csv


path = "/Users/rramkumar/Desktop/chromedriver"
browser = webdriver.Chrome(executable_path = path)
url = "https://insights.edx.org/courses/course-v1:GTx+CS1301x+1T2017/learners/"
browser.get(url)
browser.find_element_by_id('login-email').send_keys('rramk19992@gmail.com')
browser.find_element_by_id('login-password').send_keys("#####")
browser.find_element_by_css_selector('.action.action-primary.action-update.js-login.login-button').click()
df = pd.read_csv('grades.csv')
df = df[df.Grade > .10]
h = 0
print len(df['Username'])
df = df.drop(df.index[0:2217])
for i in df["Username"]:
	url2=url+"#"+i
	browser.get(url2)
	time.sleep(2)
	select = Select(browser.find_element_by_xpath('//*[@id="DataTables_Table_' +str(h) +'_length"]/label/select'))
	select.select_by_value('100')
	html = browser.page_source
	html = html.encode('utf-8')
	f = open('data/' + i + '.txt', 'w')
	f.write(html)
	f.close()
	ids = 'DataTables_Table_' +str(h)
	h+=1
	for j,df2 in enumerate(pd.read_html(html)):
		df2['username'] = i
		df2.to_csv("test.csv", index = False, mode='a')