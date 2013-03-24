#!/usr/bin/python

from redis import Redis

def __geoip_redis_aton(ip):
	try:
		x = map(int, ip.split('.'))
		return (x[0] << 24) | (x[1] << 16) | (x[2] << 8) | (x[3] << 0)
	except:
		return None

def geoip_redis(r, ip, country_only = True):
	ipnum = __geoip_redis_aton(ip)
	
	if not(ipnum):
		return None
	
	try:
		(res, score) = r.zrangebyscore("geoip", ipnum, 'inf', 0, 1, withscores=True)[0]

		(id, junk, start_end) = res.split(":", 2)

		if start_end == "s" :
			if float(score) > ipnum :
				# We have begin of new block and IP actually is not found
				return None
		
		key = "geoip:" + id
		data = r.hgetall(key)
		
		if country_only:
			return data["code"].upper()
			
		return data
	except:
		return None
	

r = Redis("localhost")

print geoip_redis(r, "194.145.63.0", False)

		
