# API KEY: 8916674ee011411aae3f5d83992abd18
import json
import time
from urllib.request import urlopen

# IBM Watson NLP libraries
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, EntitiesOptions, SentimentOptions

# NLP Authentication
authenticator = IAMAuthenticator('edJ96pfFUB2JT949IVN-aLuGIrAs75NLpfHfbw5sBB18')
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2020-08-01', authenticator=authenticator)
natural_language_understanding.set_service_url('https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/3528455f-6fa6-4e10-8eb8-1e0cdf7779e0')

def getNews(publisher, keyword):
    keyword = keyword.replace(" ", "%20") # Make it URL friendly
    url = "https://newsapi.org/v2/everything?sources=" + publisher + "&q=" + keyword + "&apiKey=8916674ee011411aae3f5d83992abd18"

    # Get the returned json and pull the info we need
    jsonurl = urlopen(url) 
    fulltext = json.loads(jsonurl.read())

    if fulltext["totalResults"] == 0:
        return "NO ARTICLES FOUND!"

    retVal = ""
    sentiments = []
    for article in fulltext["articles"]:
        title = article["title"]
        description = article["description"]

        response = natural_language_understanding.analyze(text=description,features=Features(sentiment=SentimentOptions())).get_result()
        sentimentLabel = response['sentiment']['document']['label']
        sentimentScore = response['sentiment']['document']['score']
        sentiments.append(sentimentScore)
        sentiment =  sentimentLabel + ": " + str(sentimentScore)

        retVal += (title + " SENTIMENT- " + sentiment + "<br>")
        time.sleep(1) # Necessary to have multiple API calls, o/w IBM rejects all of them

    sentimentAverage = sum(sentiments) / len(sentiments)
    if sentimentAverage > 0.0:
        retVal += ("<br> OVERALL SENTIMENT ANALYSIS: Positive- " + str(sentimentAverage))
    else:
        retVal += ("<br> OVERALL SENTIMENT ANALYSIS: Negative- " + str(sentimentAverage))
    return retVal