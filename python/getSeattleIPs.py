#!/usr/bin/env python
#-----------------------------------------------------------------------------
#joins IP Ranges to Locations and converts IP from an Int to Octets. 

import json
import csv

# converts Integer to binary (http://stackoverflow.com/questions/699866/python-int-to-binary)
# ex: toBinary(3640355304) = '11011000111110110110100111101000'
def IntToBinary(n):
	return ''.join(str(1 & int(n) >> i) for i in range(32)[::-1])

# converts binary to integer (referenced https://geekdeck.wordpress.com/2010/01/19/converting-a-decimal-number-to-ip-address-in-python/)
def BinaryToIP(b):
	return '.'.join(str(int(b[i:i+8],2) >>i) for i in range(4))


locationsFile = open('../IPGeolocation/GeoLiteCity-Location.csv','r')
# read past copywrite
locationsFile.readline()

locationsReader = csv.DictReader(locationsFile)
locations=[]
locationIDList=[]
for location in locationsReader:
	if location['city'] == 'Seattle':
		locations.append(location)
		locationIDList.append(location['locId'])

blocksFile = open('../IPGeolocation/GeoLiteCity-Blocks.csv','r')
# read past copywrite
blocksFile.readline()

blocksReader = csv.DictReader(blocksFile)
blocks=[]
for block in blocksReader:
	if block['locId'] in locationIDList:
		blocks.append(block)
	
print locations,locationIDList,blocks

