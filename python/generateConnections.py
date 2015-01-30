#!/usr/bin/python

import json

connections=[]

traceroutes=json.loads(open('traceroutesRandomSample.json','r').read())
for traceroute in traceroutes:
	routeArray=[]
	routeArray.append(traceroute['ip'])
	for route in traceroute['routes']:
		if len(route.keys()) > 0:
			routeArray.append(route['ip'])
	for i in range(0,len(routeArray)-1):
		if (routeArray[i],routeArray[i+1]) not in connections and (routeArray[i+1],routeArray[i]) not in connections:
			connections.append((routeArray[i],routeArray[i+1]))

print connections