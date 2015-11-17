# Seattle Internet Map

#### Notes from the Code for Seattle meet up on Apr 23, 2015 

* Next steps for me are:
  * Get Cencus Block data
  * Traceroute IPs from mLAB data in BigTable

## Getting Cencus Block Data: 

http://www.seattle.gov/dpd/cityplanning/populationdemographics/geographicfilesmaps/2010census/default.htm
  - http://www.seattle.gov/dpd/cs/groups/pan/@pan/documents/web_informational/dpdd017072.zip
  - http://www.seattle.gov/dpd/cs/groups/pan/@pan/documents/web_informational/dpdd017073.xlsx

Referense for shapefile conversion on mac
  http://ben.balter.com/2013/06/26/how-to-convert-shapefiles-to-geojson-for-use-on-github/

Convert the file
```sh
# From zip file convert kc_block_10.shp to GEOJSON
ogr2ogr -f GeoJSON -t_srs crs:84 kc_block_10.geojson kc_block_10.shp
```

Reading the data
```python
import json

kingCountyBlocks=json.loads(open('kc_block_10.geojson').read())
features = kingCountyBlocks['features']
len(features)
# result: 35838
features[0]['properties']['GEOID10']
# result: u'530330067001001'
# next could load Seatte neighborhoods and filter the feature list.  Still have about 15k blocks, may need to aggregate by neighborhood depending on the zoom level.
```

#### Notes from meeting with Michael Mattmiller, Bruce Blood and Tony Perez @ City of Seattle Offices on Apr 10, 2015 

Reviewed current visualizations of network topology:

```sh
cd site
python server.py
#go to http://localhost:8001/Dendogram.html
#data is in the flare.json format which is the basis for many d3.js layouts.
```

* Data was collected using one sample traceroute from each ip range in Seattle from the max mind dataset.  Scripts are in the python folder.
  * Examples include: Dendogram.html, bubble.html, bundle.html
  * Initial work on map is map.html.  Need to add layers for census tracks (I have data in geojson, but not in this repo yet)
  * Agreed to use 'Census Track' as the finest level of granularity for visualizing data.
  * Showed map showing speed test distribution using location data provided.  Can be viewed at: https://www.google.com/fusiontables/DataSource?docid=1yNMP16kUEjxPYeFXm565F9se42MVKktdDQh4g8tP
    * BigQuery queries in queries file.
* Discussed ways to get better geolocation data
  * To discuss ideas with MLab
  * Can we use a open source geolocation API?  Something like Wigle.net?
  * Could store data by census track and show the count of homes services by each logical node discovered through traceroutes.

#### Notes from meeting with Bruce Blood and Tony Perez @ City of Seattle Offices on Feb 11, 2015 

* Existing Maps
  * State map 
  * From Will Saunders - used to run broadband office
    * Now runs open data at Washington State office
  * City's goal: Equal, Affordable, Symetrical (up/down) Gigabit Internet
    * Focus on residential / small businesses
  * Chattanooga, TN is a good example to look at

** Internet in Seattle

|provider|type|notes|
|Century Link|DSL||
||Century Link Fiber||
||Centurly Link Prism (cable tv) requires 24 MB internet||
|Comcast|Cable Internet||
|Wave Broadband||Gigabit Pilot in Eastlake (600 homes)|
|Wireless Carriers|| not currently in scope|

** Regulation

  * Telco regulated by Washington State
  * Cable is regulated by the city (Tony's office)
  * On Feb 26th, it is likely that broadband as Title 2 Common Carrier
      * No bid discrimination
    * Will likely have loophools for peering

** Plan

  * Map seattle's internet infrastructure using traceroutes and the resources listed below.
  * Find a way to measure family and small businesss internet service levels.
  * Create a speed test page and ask residents to test their service.
  * Use permit data from the City of Seattle to map investments.
  * Will provide data regarding what providers offer (price / speed).

**  Technology

  Cable
    Shared medium
  DSL
  Central Office (CO) -> POP -> Twisted Copper (TC) (limit of 2,400ft)
  Upgrade model to shorten TC: 
    CO -> POP -> Cross Connect -> TC
    Some parts of town have 1.5 MB down / 300k up via DSL

** Data

* Dimensions:
  * Location
  * Service provider
  * Service description

* Measures:
  * Price
  * Advertized speed (up / down)
  * Objserved speed (up / down)
  * Time of day

* City Data
  * node locations can be obtained
  * Permits might not be in digital format due to backlog

** Ideas

 * Create heat map showing decreased speeds from POP
 * Use path-ping method to get initial speed 
 * Speed Test Page
  * Result of speed test could show their performance vs others in their area
  * Might increase bandwidth on network seattle routers
  * The city hosts videos - maybe could use their data around connection speeds from users
  * Web site is .Net
  * Could leverage a Socrata Form? (ask Chris Metcalf)

#### Notes from the Code for Seattle meet up on 1/29/15
  * not quite ready for a demo
  * almost completed traceroute collection script

#### Notes from the Code for Seattle meet up on 1/8/15

Michael Mattmiller (City of Seattle CTO) expressed the desire for a map showing real world internet service levels to residents in Seattle.  The goal of the map is to show:
  * the difference in service levels of each provider
  * the impact of infrastructure investments
  * seattle's progress towards Gigabit internet
  * the variance in service levels by neighborhood

## Ideas:

* Map seattle's internet infrastructure using traceroutes and the resources listed below
* Find a way to measure end user internet serivice levels
  * Create a speed test page and ask residents to test their service?
* Use permit data from the City of Seattle to map investments

## Resources:

* Seattle Internet Exchange:
  * http://www.seattleix.net/
  * Ex. of peers: http://www.seattleix.net/rs/rs2.1500.v4.peers.txt

* Peering / Routing info:
  * https://www.peeringdb.com
  * http://www.irr.net/docs/list.html#RADB

* Geolocation data by IP:
  * http://dev.maxmind.com/geoip/legacy/geolite/

* Mac OS X traceroute man page:
  * https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man8/traceroute.8.html

* Traceroute implemented in python
  * https://blogs.oracle.com/ksplice/entry/learning_by_doing_writing_your

* Measurement Lab
  * http://www.measurementlab.net/
  * https://cloud.google.com/bigquery/docs/dataset-mlab#schema

* gdal is used to convert shape files to GeoJSON
  * brew install gdal

* whois python library
  * https://pypi.python.org/pypi/whois

* geopy
  * https://pypi.python.org/pypi/geopy/1.7.1
  * take address from whois lookup and convert it to lat/long
