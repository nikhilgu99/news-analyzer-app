# News Analyzer App
BU EC500 Final Project

*Video Demo:* [Link](https://drive.google.com/file/d/1GvZkx-SUlZNe1gPkWl_vsfVFBVGSCgmQ/view?usp=sharing)

Flask web application to lookup keyword related news articles from various publishers and locally save them to a CSV file.

On the home page, there is a dropdown list of available news sources, and a keyword field. By default, if no publisher is selected, it will query all publishers. Articles are sorted by most recent. Depending on the number of found articles, it may 20-30 seconds to load. This is because a time delay (0.5s) is needed in order to run NLP analysis on each of the articles without getting all the API requests rejected.

*Home Page*

<img alt="Home Page" src="/static/demo/home.png">

On the results page, a table of all found articles is displayed with their Title, Sentiment, Author, Date.
Under the table is the overall sentiment of the articles, and the options to export either specific or all articles in a CSV format.

*Results Page*

<img alt="Results Page" src="/static/demo/results.png">

*CSV File*

<img alt="CSV File" src="/static/demo/csv.png">

## Future Steps
- Allow showing more results. The current is 20, max allowable by API is 100, however this would increase loading time by 5x and make table too long for readability. A possible solution for this is create pages with arrow buttons around the overall sentiment text to go through the 5 pages of potential articles.
- Create a date option to search for articles before a certain date. This was implemented, but then we found NewsAPI only allows us to query back 1 month in time with a free account, so we removed it for now.
