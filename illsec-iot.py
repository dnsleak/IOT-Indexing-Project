#usage is python2 illsec-iot.py iplist.txt portnumber. it auto outputs the data into a file named as the ip its making a request to.
import sys, os

port = int(sys.argv[2])
ips = open(sys.argv[1], "r").readlines()

for ip in ips:
    ip = ip.strip("\r\n")
    ip = ip+":"+str(port)
    cmd = "curl -I '%s' >> '%s'" % (ip, ip) #default curl request as of right now, working on setting some other juicy hooks up.
    os.system(cmd)
