#!/bin/bash

# requirements:
# pip install validators
# how to use it:
# python check-tor-exit-nodes.py [<logs-folder>|<log-file>] <exit-nodes-list>



from validators import ip_address
import sys
import re 
import os
import requests

print """                           
                        *
                    _:*///:_                     
                _+*///////////+_                
    ____----*////////////////////**----____    
   *//////////////////////////////////********    
   */////////////////       ////**************    
   *////////////////          /***************    
   *///////////////   /////   ****************    
   *//////////////   /////**   ***************    
   *//////////////   ////***   ***************    
   *//////////////   ///****   ***************    
   *////////////                 *************    
   *////////////    Saleh Bin    *************    
   *////////////     Muhaysin    *************    
   *////////////                 *************    
    *////////********************************     
     */////  github.com/salehmuhaysin  *****      
      *///*********************************             
=========================================================="""


# check if the arguments has the element <log-file> 
if len(sys.argv) != 2:
	print "[-] Error: you have to provide all the arguments: python TorDetector.py (<logs-folder>|<log-file>)"
	sys.exit()


log = sys.argv[1]
exit_node = "tor_exit_nodes.list"
exit_node_uri = "https://www.dan.me.uk/torlist/"


# check if any ip address in the log match any exit node ip address
def GetMatch(iplist , exit_nodes_list):
	hits = []
	
	for i in iplist:
		if i in exit_nodes_list and ip_address.ipv4( i ):
			print "[+] Hit: The IP [" + i + "] is an exit node"
			hits.append( i )	
	return hits


def FetchExitNodes(uri , exit_node):
	r = requests.get(uri, allow_redirects=True)
	if r.status_code == 200:
		f = open(exit_node, 'wb')
		f.write(r.content)
		f.close()
		return True
	else:
		print "[-] Failed to fetch the exit nodes"
		print "[-] Message: " + r.content
		return False

# get the list of all exit node ip addresses
def GetExitNodes(exit_node):
	f_exit_nodes = open(exit_node , 'r')
	exit_nodes_list = []
	for l in f_exit_nodes.readlines():
		l = l.strip()
		if ip_address.ipv4(l):
			exit_nodes_list.append(l)
		
	f_exit_nodes.close()
	return exit_nodes_list



# get all ip addresses from specifc file, and remove duplication
def GetLogIP(log):
	# get the content of the log file

	f = open(log , 'r')
	log_content = f.read()
	f.close()

	# find all ip addresses in the log file and remove duplicate
	iplist = re.findall( r'[0-9]+(?:\.[0-9]+){3}', log_content )
	iplist = list(set( iplist ))
	
	return iplist


# this will execute the code for each specific file of log
def main(log , exit_node ):
	if exit_node_uri != "":
		FetchExitNodes(exit_node_uri , exit_node)
		
	if os.path.exists(exit_node):
		print "[+] file ["+exit_node+"] exists, will used old tor exit node list"
	else:
		return []
		
	exit_nodes_list = GetExitNodes(exit_node)
	iplist 		= GetLogIP(log)
	hits 		= GetMatch(iplist , exit_nodes_list)
	
	# get all results
	result = []
	for i in hits:
		result.append( str("[+] Hit: The IP [" + i + "] is an exit node, from file: " + log) ) 

	return result

loglist = []
if os.path.isfile(log):
	loglist.append(log)

elif os.path.isdir(log):
	for f in os.listdir(log):
		loglist.append(log + '/' + f)


res = []
for logfile in loglist:
	print "[+] Checking the file: " + logfile
	for m in main(logfile, exit_node):
		res.append( m )


print "[+] Number of hits " + str(len(res))
for r in res:
	print r







