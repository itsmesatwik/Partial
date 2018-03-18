from newsapi import NewsApiClient
from apiKey import newsapikey


def getArticlesList(keyword, date):
    api = NewsApiClient(api_key = newsapikey)
    top_headlines = (q= apiKeyword,
            language= 'en',
            country= 'us')
    return top_headlines

