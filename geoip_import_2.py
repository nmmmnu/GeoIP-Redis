#!/usr/bin/python

filename     = "data/GeoLite2-Country-CSV_20150407/GeoLite2-Country-Blocks-IPv4.csv"
filename_loc = "data/GeoLite2-Country-CSV_20150407/GeoLite2-Country-Locations-en.csv"

from redis import Redis
r = Redis("localhost")

from geoip_ipcalc import IPCalc

count = 0

for line in open(filename):

	try:
		x = line.strip().split(",")
	except:
		pass
	
	if len(x) < 6 :
		continue

	if x[0] == "network" :
		continue

	ip = x[0]
	
	xx = ip.split("/")
	
	ipc = IPCalc(xx[0], int(xx[1]))
	
	num_start = ipc.getStartIP()
	num_end   = ipc.getEndIP()

	id = x[1]
		
	key = id + ":" + str(count)

	r.zadd("geoip", key + ":s", num_start)
	r.zadd("geoip", key + ":e", num_end)

	count = count + 1
	if count % 1000 == 0 :
		print "Imported %8d" % count

count2 = count



count = 0

for line in open(filename_loc):
	x = line.strip().split(",")

	if len(x) < 6 :
		continue
	
	if x[0] == "geoname_id" :
		continue

	(id, lang, continent, continent2, code, country) = x
		
	dic = {}
	
	dic["id"] = id
	
	if code :
		dic["code"]	= code

	if country :
		dic["country"]	= country

	key = id

	r.hmset("geoip:" + key, dic)

	count = count + 1
	if count % 1000 == 0 :
		print "Imported %8d" % count

print "Done %d subnets imported" % count2
print "Done %d locations imported" % count
