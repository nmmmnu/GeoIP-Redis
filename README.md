GeoIP-Redis
===========

Put GeoIP database in Redis

Please refer to 
   readme.html or
   http://redis4you.com/articles.php?id=018&name=GeoIP+in+Redis

Update 2015-MAY
===============

Some time ago GeoIP changed the CSV format. 
While old CSV format is still updated and downloadable, we are included **geoip_import_2.py**
that import both GeoLite2-Country and GeoLite2-City.

GeoLite2-Country uses numerical ID's, so you can not import without hashes.

