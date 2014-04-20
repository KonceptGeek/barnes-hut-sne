import json
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import numpy
import sys

def readData(filename):
    jsonObjects = []
    jsonMap = {}
    with open(filename) as jsonFile:
        for (i,line) in enumerate(jsonFile):
            line = line.strip('\n\r')
            if line:
                jsonObject = json.loads(line)
                assert jsonObject['description']
                #jsonObjects.append(jsonObject)
                text = jsonObject['description']
                jsonMap[text.lower().strip()] = jsonObject
    for (key,value) in jsonMap.iteritems():
        jsonObjects.append(value)
    return jsonObjects[:15000]

def extBagOfWordFeatures(jsonObjects):
    corpus = []
    stop = set(stopwords.words("english"))
    for jsonObject in jsonObjects:
        text = jsonObject['descriptionTokenized']
        text = text.lower()
        filteredWords = ' '.join([w for w in text.split() if not w in stop])
        corpus.append(filteredWords)
    
    vectorizer = CountVectorizer(min_df=0,dtype='Float64')
    X = vectorizer.fit_transform(corpus)
    return X

