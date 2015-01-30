#!/usr/bin/env python
#-----------------------------------------------------------------------------
#joins IP Ranges to Locations and converts IP from an Int to Octets. 

import json
import csv

# converts Integer to binary (http://stackoverflow.com/questions/699866/python-int-to-binary)
# ex: toBinary(3640355304) = '11011000111110110110100111101000'
def IntToBinary(n):
	return ''.join(str(1 & int(n) >> i) for i in range(32)[::-1])

# converts binary to integer
# binary is a 32 character string such as '11011000111110110110100111101000'
# each 8 bytes represents each octet in the IP address
# '11011000111110110110100111101000' becomes ['01001010', '01111101', '00101011', '01100011']
# then convert each string to an integer int(n,2)
def BinaryToIP(b):
	return '.'.join(map(lambda i: str(int(b[i*8:(i*8)+8],2)), range(4)))

def IntToIP(int):
	return IntToBinary(BinaryToIP(int))


locationsFile = open('../IPGeolocation/GeoLiteCity-Location.csv','r')
# read past copywrite
locationsFile.readline()

locationsReader = csv.DictReader(locationsFile)
locations={}
for location in locationsReader:
	if location['city'] == 'Seattle':
		locations[location['locId']] = location

blocksFile = open('../IPGeolocation/GeoLiteCity-Blocks.csv','r')
# read past copywrite
blocksFile.readline()

blocksReader = csv.DictReader(blocksFile)
blocks=[]
for block in blocksReader:
	if block['locId'] in locations.keys():
		newBlock=block
		newBlock['startIp']=BinaryToIP(IntToBinary(block['startIpNum']))
		newBlock['endIp']=BinaryToIP(IntToBinary(block['endIpNum']))
		newBlock['location']=locations[block['locId']]
		blocks.append(block)	
	
outputFile = open('seattleCIDRBlocksAndLocations.json','w')

outputFile.write(json.dumps(blocks))
outputFile.close()

