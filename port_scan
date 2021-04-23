#Port Scanning script
#Mackenzie Summers
#Run from Win10

import argparse
import socket
import requests
import time
 
def scanMe(user_args):
	target_host = "10.12.0.30"
	port_list = [*range(100)]
	#port_list = [80]
	quiet = True
	timeout = 0
	results = {target_host:[]}
	protos = ["ftp","ssh", "smtp", "telnet", "web"]
	known_ports = [21,22,23,25,80]
	version_list = {}
 
	if user_args.get("wait") != 0:
		timeout = user_args.get("wait")
	print("Starting Scan\n")
	for target_port in port_list:
		try:
			print("Scanning Port: {}".format(target_port))
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect((target_host, target_port))
			data = client.recv(4096)
			data = data.decode("ascii")
			test = len(data)
			if test > 0:
				for proto in protos:
					if proto in data.lower() or port in known_ports:
						version_list.update({proto: data})
						break
			new_host = [target_port, "O"]
			results[target_host].append(new_host)
			time.sleep(timeout)
		except Exception as e:
			new_host = [target_port, "C"]
			results[target_host].append(new_host)
			time.sleep(timeout)
		client.close()
	print("\nPort Type: TCP")
	print("Target" + " "*(25-6) + "Port" + " "*(25-4) + "Status\n")
	for key in results.keys():
		target_final_list = results.get(key)
		for item in target_final_list:	
			if item[1] == "O":
				print(key + " "*(25 - len(key))+ str(item[0]) + " "*(25 - len(str(item[0]))) + "Open\n")
			elif quiet == False:
				print(key + " "*(25 - len(key))+ str(item[0]) + " "*(25 - len(str(item[0]))) + "Closed\n")		
	print("Version Information for Open Ports")
	print("Service: {}Version: ".format(" "*25))
	for item in version_list.items():
		print("{}{}{}".format(item[0], " "*(25 - len(item[0])), item[1]))
	return
 
parser = argparse.ArgumentParser()
parser.add_argument("-W", "--wait", help = "specifies a time to time.sleep between each scan: max of 60 seconds", type = int, choices = range(0, 60), metavar = "{0...60}", default = 0)
 
args = parser.parse_args()
args_dict = vars(args)
scanMe(args_dict)
