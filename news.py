# API KEY: 8916674ee011411aae3f5d83992abd18
import json
from urllib.request import urlopen

def getNews(publisher, keyword):
    keyword = keyword.replace(" ", "%20")
    url = "https://newsapi.org/v2/everything?sources=" + publisher + "&q=" + keyword + "&apiKey=8916674ee011411aae3f5d83992abd18"

    # Get the returned json and pull the info we need
    jsonurl = urlopen(url) 
    fulltext = json.loads(jsonurl.read())

    if fulltext["totalResults"] == 0:
        return "NO ARTICLES FOUND!"

    retVal = ""
    for article in fulltext["articles"]:
        description = article["description"]
        retVal += (description + "<br>")

    return retVal