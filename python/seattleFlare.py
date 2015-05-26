import json

connections = json.loads(open("sampleRouteConnections.json").read())

levelOne = {}
for name, values in connections.iteritems():
  if values["DOWNcount"]==0 and values["UPcount"]==1:
    if name in levelOne.keys():
      levelOne[name]["size"]= levelOne[name]["size"] +1
    else:
      levelOne[name] = {"name": name, "size": 1}

def processList(oldList):
  newList={}
  for k,v in oldList.iteritems():
    if "leafStart" not in v.keys():
      match=False
      for name, values in connections.iteritems():
        if k in values["DOWNconnections"] and values["UPcount"]==1:
          match=True
          if name in newList.keys():
            newList[name]["size"]= newList[name]["size"] +1
            newList[name]["children"].append(oldList[k])
          else:
            newList[name] =  {"name": name, "size": 1, "children": [oldList[k]]}
      if match==False:
        newList[k]=oldList[k]
        newList[k]["leafStart"]=True
    else:
      if k in newList.keys():
        newList[k]["size"]= newList[k]["size"] +1
        newList[k]["children"].append(oldList[k])
      else:
        newList[k] =  oldList[k]
  return newList

currentKeyCount=0
previousKeyCount=len(levelOne.keys())
loopCount=0
inputList=dict(levelOne)
while previousKeyCount!=currentKeyCount or loopCount>20:
  previousKeyCount=len(inputList.keys())
  inputList=processList(inputList)
  currentKeyCount=len(inputList.keys())
  loopCount=loopCount+1
  print loopCount, currentKeyCount

outputList=[]

for k,v in inputList.iteritems():
  outputList.append(v)

output={"name": "home", "children": outputList}
outputFile=open("seattleFlare.json","w")
outputFile.write(json.dumps(output))
outputFile.close