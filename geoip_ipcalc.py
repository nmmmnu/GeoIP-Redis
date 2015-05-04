
class IPCalc:
	def __init__(self, ip, mask):
		self.ip = ip
		self.mask = mask
	
	def getStartIP(self):
		i = self._aton();
		m = (1 << self.mask) - 1
		m = m << (32 - self.mask)

		return i & m
		
	def getEndIP(self):
		i = self._aton();
		m = (1 << self.mask) - 1
		m = m << (32 - self.mask)

		m1 = (1 << (32 - self.mask)) - 1;
		
		return i & m | m1

	def _aton(self):
		try:
			x = map(int, self.ip.split('.'))
			return (x[0] << 24) | (x[1] << 16) | (x[2] << 8) | (x[3] << 0)
		except:
			return None


if False:
	x = IPCalc("4.3.2.1", 30)

	print "%x - %x\n" % (x.getStartIP(), x.getEndIP())

