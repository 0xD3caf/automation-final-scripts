#OS Defensive Vulnerability Search
#Mackenzie Summers
#Run from Root Kali Account
 
import os, subprocess, re
 
def vuln_search():
	cron_list = []
	user_list = []
 
	#OS Version
	out = subprocess.Popen(["cat", "/etc/os-release"], 
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT)
	stdout,stderror = out.communicate()
	stdout = stdout.decode("ascii")			
	outputs = stdout.split("\n")
	OS_name = outputs[0].split("=")[1]
	regex_str = 'VERSION="\w*\.?\w*"'
	sys_version = re.search(regex_str, stdout)
	remove_vers = sys_version.group().split("=")[1].strip('"')
	print("Operating system is: {}".format(OS_name.strip('"')))
	print("     OS verison: {}".format(remove_vers))
 
	#Kernel Version
	out = subprocess.Popen(["uname", "-r"],			
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT)
	stdout,stderror = out.communicate()
	print("     Kernel verison: {}".format(stdout.decode("ascii")))
 
	#Set UID Bits
	os.system("find /bin -perm -4000 1> UID.txt 2>/dev/null")		
	print("For listing of UID Bits see UID.txt file")
 
	#Get List of Users
	out = subprocess.Popen(["cat", "/etc/passwd"],			
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT)
	stdout, stderror = out.communicate()
	stdout = stdout.decode("ascii")
	lines = stdout.split("\n")
	for line in lines:
		user_list.append(line.split(":")[0])
 
	#Get Cron Jobs for ALL Users
	print("\nCurrent Cron Jobs")
	for user in user_list:
		user_crob_jobs = []
		user = user.strip()
		user_string = "-u{}".format(user)
		out = subprocess.Popen(["crontab",user_string , "-l"],			
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT)
		stdout,stderror = out.communicate()
		if "no" not in str(stdout):
			print("User {} Cron Jobs".format(user))
			print(str(stdout.decode("ascii")))
 
	#SSH Keys
	print("\nSSH Keys")
	keys = []
	key_loc = "/etc/ssh/"
	files = os.listdir(key_loc)
	for file in files:
		if "key" in file.lower():	
			out = subprocess.Popen(["ssh-keygen", "-l", "-f", (key_loc + file)],			
				stdout=subprocess.PIPE,
				stderr=subprocess.STDOUT)
			stdout,stderror = out.communicate()
			stdout = stdout.decode("ascii")
			if stdout.strip() not in keys:
				keys.append(stdout.strip())
 
	for item in keys:
		print("Key Found: {}".format(item))
	#Running Processes
	os.system("ps -aux > process.txt")				
	print("\nFor a listing of processes please see process.txt")
 
	#Sockets
	os.system('echo "" > sockets.txt')
	os.system("netstat -lt >> sockets.txt")
	os.system("netstat -lu >> sockets.txt")
	print("For a list of Sockets see sockets.txt")
 
print("\nVulnerability Search\n")
vuln_search()
