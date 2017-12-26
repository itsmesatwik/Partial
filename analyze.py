import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='username',
  password='password',
  version='2017-02-27')

response = natural_language_understanding.analyze(
  url='www.ibm.com',
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

print(json.dumps(response, indent=2))