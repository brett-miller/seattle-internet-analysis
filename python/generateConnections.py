#!/usr/bin/python

import json
from sets import Set

connections={}
connectionNodes=Set()
sourceNodes=Set()
targetNodes=Set()

traceroutes=json.loads(open('traceroutesRandomSample.json','r').read())
for traceroute in traceroutes:
	routeArray=[]
	routeArray.append(traceroute['sampleIp'])
	for route in traceroute['sampleIpTraceroute']['routes']:
		if len(route.keys()) > 0:
			routeArray.append(route['name'])
	for ix, route in enumerate(routeArray):
		if route not in connections.keys():
			connections[route] = { "DOWNcount": 0, "UPcount": 0, "UPconnections": [],"DOWNconnections": [], "name": routeArray[ix] }
		if ix > 0 and routeArray[ix-1] not in connections[route]["UPconnections"]:
			connections[route]["UPconnections"].append(routeArray[ix-1])
			connections[route]["UPcount"] = connections[route]["UPcount"] + 1
		if ix < (len(routeArray)-1) and routeArray[ix+1] not in connections[route]["DOWNconnections"]:
			connectionNodes.add((route, routeArray[ix+1]))
			sourceNodes.add(route)
			targetNodes.add(routeArray[ix+1])
			connections[route]["DOWNconnections"].append(routeArray[ix+1])
			connections[route]["DOWNcount"] = connections[route]["DOWNcount"] + 1
				
levelOne={}
levelOneCount=[]
for k,v in connections.iteritems():
	if v["UPcount"] > 1:
		levelOne[k] = v
		levelOneCount.append((v["UPcount"],k))

levelOneCountSorted = sorted(levelOneCount, reverse=True)
levelOneCountSortedList = list(connectionNodes)
filteredList = []
for item in levelOneCountSortedList:
	if item[1] in list(sourceNodes) and item[0] in list(targetNodes) and item[1] != item[0]:
		filteredList.append(item)


topOne={}
for ip in connections[levelOneCountSorted[0][1]]["UPconnections"]:
	if connections[ip]["UPcount"] > 1:
		topOne[ip] = connections[ip]


outputFile = open('sampleRouteConnections.json','w')
outputFile.write(json.dumps(connections))
outputFile.close()

outputFile = open('levelOne.json','w')
outputFile.write(json.dumps(levelOne))
outputFile.close()

outputFile = open('connectionNodes.json','w')
outputFile.write(json.dumps(filteredList))
outputFile.close()



