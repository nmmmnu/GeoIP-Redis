#!/usr/bin/python

filename = "GeoIPCountryWhois.csv"

from redis import Redis
r = Redis("localhost")

count = 0

for line in open(filename):
	x = line.strip().split(",")

	if len(x) < 6 :
		continue
	
	for i in range(len(x)) :
		if i < 6 :
			x[i] = x[i].replace("\"", "")
		else :
			x.pop()

	(ip_start, ip_end, num_start, num_end, id, country) = x

	#print "%10s %10s %2s" % (num_start, num_end, id)
	
	key = id + ":" + str(count)
	
	r.zadd("geoip", key + ":s", num_start)
	r.zadd("geoip", key + ":e", num_end)

	r.hmset("geoip:" + id, {
		"code"		: id		,
		"country"	: country
	})

	count = count + 1
	if count % 1000 == 0 :
		print "Imported %8d" % count

print "Done %d subnets imported" % count

