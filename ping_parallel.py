#!/usr/bin/python

import re
from subprocess import Popen, STDOUT, PIPE

def net_ping(ips):
	procs = []
	ret = {}
	ret2 = []
	for ip in ips:
		procs.append(Popen(('ping','-c2','-n','-w5','-i0.3',ip), stdout=PIPE, stderr=STDOUT))
	for pr in procs:
		out = str(pr.communicate()[0])
		if 'bytes from' in out:
			# extract IP
			ip = re.search(r'([\d]+.[\d]+.[\d]+.[\d]+)', out).groups()[0]
			ret2.append(ip)
			ret[ip] = float(re.search(r'min/avg/max/mdev = [\d.]+/([\d.]+)', out).groups()[0])
	return ret2

def net_range():
	net = []
	#change range of DD, where AA.BB.CC.DD
	for ip in range(1,254):
		#change ip range for yourself in next format AA.BB.CC.
		net.append("10.0.0." + str(ip))
	return net

print net_ping(net_range())
