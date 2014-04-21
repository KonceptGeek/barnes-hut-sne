import json

def readData(filename):
	minx = 0
	maxx = 0
	miny = 0
	maxy = 0
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
	print "MinX - " + str(minx)
	print "MaxX - " + str(maxx)
	print "MinY - " + str(miny)
	print "MaxY - " + str(maxy)

readData('output/coordinateslensing-10000-p30.json')