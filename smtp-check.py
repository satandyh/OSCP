#!/usr/bin/python

#we will use cmd style of our script - just for practice in python and for usability
import sys,getopt,socket,fileinput

#split cmd strings and filelines in one list
def get_data(data,datafile):
	result = []
	if datafile:
		with open(datafile) as f:
			result = f.readlines()
			result = [x.strip('\n') for x in result]
	if data:
		result.append(data)
	return result

#function "user_verify" that try to verify all users from file or cmd at one separate ip
#need to do this function parallel
def user_verify(ip,port,userlist):
	result = []
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip,port))
		s.recv(1024)
	except:
		print 'Oops can\'t connect to '+ip+' with port '+str(port)
	for user in userlist:
		s.send('VRFY '+user+'\r\n')
		res = s.recv(1024)
		#print res
		if "250" in res:
			result.append(user)
		elif "252" in res:
			#result.append(user)
			result
	s.close()
	return result

#function "check_ip" calls function user_verify on all server ips from file or cmd
#try to do it parallel
def check_ip(ips,port,userlists):
	result = []
	for ip in ips:
		users = user_verify(ip,port,userlists)
		if users:
			result.append([ip,users])
	return result

def main(argv):
	server = ''
	serverlist = ''
	port = 25
	username = ''
	usernamelist = ''

	try:
		opts, args = getopt.getopt(argv,"hs:S:p:u:U:",["server=","Serverlist=","port=","username=","Usernamelist="])
	except getopt.GetoptError:
		print 'smtp-check.py -s <server> -S <Serverlist> -p <port> -u <username> -U <Usernamelist>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'smtp-check.py -s <server> -S <Serverlist> -p <port> -u <username> -U <Usernamelist>'
			sys.exit(1)
		if opt in ('-s','--server'):
			server = arg
		if opt in ('-S','--Serverlist'):
			serverlist = arg
		if opt in ('-p','--port'):
			port = int(arg)
		if opt in ('-u','--username'):
			username = arg
		if opt in ('-U','--Usernamelist'):
			usernamelist = arg
	
	#main process here
	userlist = get_data(username,usernamelist)
	iplist = get_data(server,serverlist)
	check = check_ip(iplist,port,userlist)
	print check

if __name__ == "__main__":
	main(sys.argv[1:])
