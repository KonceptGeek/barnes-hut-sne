import featureExtraction
import json
from itertools import izip
import unicodedata
import sys

def readCoordinateJson(filename):
	with open(filename) as inFile:
		for line in inFile:
			line = line.strip('\n\r')
			if line:
				line = line.split('jsonstr = ')[1]
				jsonObjects = json.loads(line)
	return jsonObjects


coordinateObjs = readCoordinateJson('output/coordinateslensing-full-srl-p40.json')
titles = range(0,len(coordinateObjs))
fullDataObjs = featureExtraction.readData('data/fullData.json')[:len(titles)]

finalData = {}
for (fdObj, title) in izip(fullDataObjs, titles):
	coordinateObj = coordinateObjs[str(title)]
	assert coordinateObj
	for e in fdObj['event']:
		if isinstance(e, basestring):
	            event = e
                    break
        text = fdObj['description']
	coordinateObj['event'] = event
	coordinateObj['text'] = text
	finalData[str(title)] = coordinateObj

with open('output/coordinate-srl-full-p40.json','w') as outFile:
	jsonStr = json.dumps(finalData)
	outFile.write('jsonstr = ')
	outFile.write(jsonStr+'\n')
