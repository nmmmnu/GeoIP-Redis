#!/usr/bin/python

filename     = "GeoLiteCity_20130305/GeoLiteCity-Blocks.csv"
filename_loc = "GeoLiteCity_20130305/GeoLiteCity-Location.csv"

from redis import Redis
r = Redis("localhost")

count = 0

for line in open(filename):

	try:
		x = line.strip().split(",")
	except:
		pass
	
	if len(x) < 3 :
		continue

	if x[0] == "startIpNum" :
		continue
	
	for i in range(len(x)) :
		if i < 3 :
			x[i] = x[i].replace("\"", "")
		else :
			x.pop()

	(num_start, num_end, id) = x
		
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

	if len(x) < 9 :
		continue
			
	for i in range(len(x)) :
		if i < 9 :
			x[i] = x[i].replace("\"", "")
		else :
			x.pop()

	(id, code, state, city, zip, latitude, longtinude, junk1, junk2) = x
		
	dic = {}
	
	if code :
		dic["code"]	= code

	if state :
		dic["state"]	= state
		
	if city :
		dic["city"]	= city

	if zip :
		dic["zip"]	= zip

	if code :
		dic["code"]	= code

	if latitude :
		dic["latitude"]	= latitude

	if longtinude :
		dic["longtinude"] = longtinude

	key = id

	r.hmset("geoip:" + key, dic)

	count = count + 1
	if count % 1000 == 0 :
		print "Imported %8d" % count

print "Done %d subnets imported" % count2
print "Done %d locations imported" % count
