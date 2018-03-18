import requests
from apiKey import newsapikey

def getArticlesList(keyword, date):
    apiKeyword = 'q=' + keyword + '&'
    apiDate = 'from=' + date + '&'
    apiKey = 'apiKey=' + newsapikey
    url = ('https://newsapi.org/v2/top-headlines?'
            apiKeyword
            apiDate
            'sortBy=popularity&'
            apiKey)
    response = requests.get(url)
    print response.json


