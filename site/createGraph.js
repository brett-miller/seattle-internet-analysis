
var nodes = [], links =[];
var processLevel = function(previousLevel)
{
	console.log(previousLevel);
	newLevel = {};
	newLevel.items = [];
	previousLevel.items
		.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { newLevel.items.push(data[d.UPconnections[0]])} })
	newLevel.map = d3.nest()
		.key(function(d) { return d.name })
		.rollup(function(d) { return d.length })
		.map(newLevel.items, d3.map)
	newLevel.map
		.entries()
		.forEach(function(d) { 
			nodes.push({ name: d.key, count: d.value });
			data[d.key].DOWNconnections.forEach(function(e) {
				if (previousLevel.map.has(e)) {
					links.push({ source: d.key, target: e })
				}
			});
		});
	return newLevel;
}

//Level 1
levelOne = {};
levelOne.items = [];
levelOne.map = d3.map();
Object.keys(data)
	.map(function(d) { return data[d] })
	.forEach(function(d) { if (d.DOWNconnections==0 && d.UPconnections.length == 1) { levelOne.items.push(d)} })

var levels=[levelOne];
var hasItems = true;
while (hasItems == true)
{
	levels.push(processLevel(levels.slice(-1)));
	if (levels.slice(-1).items.length == 1) {
		hasItems=false;
	}
}






//Level 2
levelTwo = [];
levelOne
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelTwo.push(data[d.UPconnections[0]])} })

levelTwoMap = d3.nest()
	.key(function(d) { return d.name })
	.rollup(function(d) { return d.length })
	.map(levelTwo,d3.map)
levelTwoMap
	.entries()
	.forEach(function(d) { 
		nodes.push({ source: d.key, count: d.value });
	});

//Level 3
levelThree = [];
levelTwo
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelThree.push(data[d.UPconnections[0]])} })
levelThreeMap = d3.nest()
	.key(function(d) { return d.name })
	.rollup(function(d) { return d.length })
	.map(levelThree, d3.map)
levelThreeMap
	.entries()
	.forEach(function(d) { 
		nodes.push({ name: d.key, count: d.value });
		data[d.key].DOWNconnections.forEach(function(e) {
			if (levelTwoMap.has(e)) {
				links.push({ source: d.key, target: e })
			}
		});
	});

//Level 4
levelFour = [];
levelThree
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelFour.push(data[d.UPconnections[0]])} })

//Level 5
levelFive = [];
levelFour
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelFive.push(data[d.UPconnections[0]])} })


//Level 6
levelSix = [];
levelFive
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelSix.push(data[d.UPconnections[0]])} })

//Level 7
levelSeven = [];
levelSix
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelSeven.push(data[d.UPconnections[0]])} })

//Level 8
levelEight = [];
levelSeven
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelEight.push(data[d.UPconnections[0]])} })

//Level 9
levelNine = [];
levelEight
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelNine.push(data[d.UPconnections[0]])} })

//Level 10
levelTen = [];
levelNine
	.forEach(function(d) { if (data[d.UPconnections[0]].UPcount == 1) { levelTen.push(data[d.UPconnections[0]])} })



