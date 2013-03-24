#!/usr/local/bin/php
<?
function geoip_redis($r, $ip, $country_only = true){
	$ipnum = ip2long($ip);

	if (! $ipnum )
		return false;
		
	$ipnum = sprintf("%u", $ipnum);
	
	$res = $r->zrangebyscore("geoip", $ipnum, "inf", array("withscores" => true, "limit" => array(0, 1) ) );

	$k = array_keys($res);
	$k = $k[0];
	$score = $res[$k];

	list($id, $junk, $start_end) = explode(":", $k);

	if ($start_end == "s")
		if ($score > $ipnum){
			// We have begin of new block and IP actually is not found
			return false;
		}
		
	$key = "geoip:" . $id;
	$data = $r->hgetall($key);
		
	if ($country_only)
		return strtoupper($data["code"]);
			
	return $data;
}

$r = new Redis();
$r->connect("localhost");
print_r( geoip_redis($r, "194.145.63.0", false) );

		
