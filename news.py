# API KEY: 8916674ee011411aae3f5d83992abd18
import json
from urllib.request import urlopen

def getNews(publisher, keyword):
    keyword = keyword.replace(" ", "%20")
    url = "https://newsapi.org/v2/everything?q=" + keyword + "&apiKey=8916674ee011411aae3f5d83992abd18"

    jsonurl = urlopen(url)
    fulltext = json.loads(jsonurl.read())

    return fulltext