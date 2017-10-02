#!/usr/bin/python

import sys,getopt,smtplib,fileinput

def main(argv):
	server = ''
	serverlist = ''
	port = '25' # default
	timeout = '5' # default
	username = ''
	usernamelist = ''

	try:
		opts, args = getopt.getopt(argv,"hs:S:pu:U:",["server=","Serverlist=","port=","username=","Usernamelist="])
	except getopt.GetoptError:
		print 'smtp-check.py -s <server> -S <Serverlist> -p <port> -u <username> -U <Usernamelist>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'smtp-check.py -s <server> -S <Serverlist> -p <port> -u <username> -U <Usernamelist>'
			sys.exit(1)
		elif opt in ('-s','--server'):
			server = arg
		elif opt in ('-S','--Serverlist'):
			serverlist = arg
		elif opt in ('-p','--port'):
			port = arg
		elif opt in ('-u','--username'):
			username = arg
		elif opt in ('-U','--Usernamelist'):
			usernamelist = arg



        conn = smtplib.SMTP(server,port)
        #conn.set_debuglevel(True)
        try:
                result = conn.verify(username)
        finally:
                conn.quit()
        print result

if __name__ == "__main__":
        main(sys.argv[1:])


def get_data(data,datafile):
	result = []
		if datafile:
			with open(datafile) as f:
				result = f.readlines()
				result = [x.strip('\n') for x in result]
		elif data:
			result.append(data)
	return result


#define function named "user_verify" that try to verify all users from file or cmd at one separate ip
#do this function parallel

#define function named "several_ip" that will do parallel call function user_verify on all server ips from file or cmd
