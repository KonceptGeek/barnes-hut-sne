import json
import unicodedata

def readData(filename):
	minx = 0
	maxx = 0
	miny = 0
	maxy = 0
	events = []
	with open(filename) as inFile:
		for line in inFile:
			line = line.strip('\n\r')
			if line:
				linesplit = line.split('jsonstr = ')
				jsonObjects = json.loads(linesplit[1])
				for key in jsonObjects.keys():
					if minx > jsonObjects[key]['x']: minx = jsonObjects[key]['x']
					if maxx < jsonObjects[key]['x']: maxx = jsonObjects[key]['x']
					if miny > jsonObjects[key]['y']: miny = jsonObjects[key]['y']
					if maxy < jsonObjects[key]['y']: maxy = jsonObjects[key]['y']
					events.append(unicodedata.normalize('NFKD', jsonObjects[key]['event']).encode('ascii','ignore'))
	print "MinX - " + str(minx)
	print "MaxX - " + str(maxx)
	print "MinY - " + str(miny)
	print "MaxY - " + str(maxy)
	#print set(events)
	print len(set(events))
readData('output/coordinate-srl-15000-p30.json')