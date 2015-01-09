
Notes from the Code for Seattle meet up on 1/8/15

Michael Mattmiller (City of Seattle CTO) expressed the desire for a map showing real world internet service levels to residents in Seattle.  The goal of the map is to show:
  * the difference in service levels of each provider
  * the impact of infrastructure investments
  * seattle's progress towards Gigabit internet
  * the variance in service levels by neighborhood

Ideas:

* Map seattle's internet infrastructure using traceroutes and the resources listed below
* Find a way to measure end user internet serivice levels
  * Create a speed test page and ask residents to test their service?
* Use permit data from the City of Seattle to map investments

Resources:

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



