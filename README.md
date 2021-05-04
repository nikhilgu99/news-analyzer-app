# News Analyzer App
BU EC500 Final Project

Flask web application to lookup keyword related news articles from various publishers and locally save them to a CSV file.

On the home page, there is a dropdown list of available news sources, and a keyword field. Depending on the number of found articles, it may 20-30 seconds to load. This is because a time delay (0.5s) is needed in order to run NLP analysis on each of the articles without getting all the API requests rejected.

*Home Page*

<img alt="Home Page" src="/static/demo/home.png">

On the results page, a table of all found articles is displayed with their Title, Sentiment, Author, Date.
Under the table is the overall sentiment of the articles, and the options to export either specific or all articles in a CSV format.

*Results Page*

<img alt="Results Page" src="/static/demo/results.png">

*CSV File*

<img alt="CSV File" src="/static/demo/csv.png">