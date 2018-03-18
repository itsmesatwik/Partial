import json
import os
from apiKey import keyname, keypas, keyver
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions,EmotionOptions,KeywordsOptions,ConceptsOptions,SentimentOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username= keyname,
  password= keypas,
  version= keyver)

def analyze(links):
  for link in links:
    response = natural_language_understanding.analyze(
      url=link,
      features=Features(
      	entities=EntitiesOptions(
          emotion=True,
          sentiment=True,
          limit=15),
      	emotion=EmotionOptions(
          targets= ['keyword1','keyword2']),
        keywords=KeywordsOptions(
          emotion=True,
          sentiment=True,
          limit=2),
        concepts=ConceptsOptions(
          limit=5),
        sentiment=SentimentOptions(
          targets=['stocks']),
        categories=CategoriesOptions()))

#Create json to store results of Watson analysis.
dir = os.path.dirname(__file__)
path = 'analysisResults.json'
file_path = os.path.join(dir, path)
with open(file_path, 'w') as outfile:
  json.dump(response, outfile, indent = 2)

