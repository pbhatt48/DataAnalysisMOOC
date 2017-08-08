# OMSCS6460


## CS1301x Data Analysis

### Python Scrips To get data (In order used):

#### Final result: resources/summary_grade_engagement.csv

|Python Script Name | Description|
| ------------ | ----------- |
| test2.py| Selenium script to scrape HTML to get user engagement data. Outputs a .txt file per user of page HTML|
| htmlToCsv.py | converts the html files into a single csv file |
| grade_engagement.py | combines engagement data with user's grade |
| summarize.py | aggregates engagement data to a single value per user per category (video, problems, discussion) |

#### Inputs 

Grades.csv (grades for all users)

#### Output: 

#### Grade and Engagment CSVs (summary_grade_engagement.csv)
| Name | DataType | Description |
| ---- | -------- | ----------- |
|username | Sting | Students Username |
|Grade | Float | Students grade in course |
|Discussions | int | Number of discussion posts |
|Problems  | int | number of problems completed |
|Videos | int | number of videos watched  |


### Python Scripts to summarize data

|Python Script Name | Description|
| ------------ | ----------- |
| summarize.py | creates regression graphs |
| DataAnalysisV10.py | calculated engagment averages per user based on letter Grade | 

## Survey Analysis

### Python Scripts

|Python Script Name | Description|
| ------------ | ----------- |
| DataWrangler.py| Python script to analyse results of the survey |






