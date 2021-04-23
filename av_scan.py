#Anitvuris / Malware Test
#Mackenzie Summers
 
#Connects via SSH to target box and locates files
#then scans files and checks for malware
#Run from Win10
 
import requests, hashlib, time, os, paramiko
from time import sleep
 
def scan(dir):
	hits = 0
	total_checked = 0
	client = paramiko.SSHClient()													
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect("10.12.0.30", username="root", password="password")
	sftp = client.open_sftp()
	sftp.chdir(dir)
	file_list = sftp.listdir()
	API_KEY = "VALUE"
	scan_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
	report_url = 'https://www.virustotal.com/vtapi/v2/file/report'
	for file in file_list:
		f = sftp.file(file, mode='r')
		files = {'file': (file ,f)}
		try:
			response = requests.post(scan_url, files=files, params={'apikey': API_KEY})
			response_data = response.json()
			resource = response_data.get("resource")
		except:
			print("looks like this file didnt work")
		for i in range(6):	
			try:
				resp = requests.get(report_url, params={'apikey': API_KEY, 'resource': resource})
				resp = resp.json()
				total_checked = resp.get("total") 
				hits = resp.get("positives")
				break
			except:
				sleep(5)
				continue
		f.close()
		if hits == 0:
			percent = 0
		else:
			percent = total_checked/hits
		if percent >= .05:
			print("MALWARE FOUND")
			print("File: {} is Malware".format(str(file)))
			sftp.close()		#
			client.close()		#
			break				#remove for full scan even after malware found
		else:
			sleep(15)
	if sftp:
		sftp.close()
	if client:
		client.close()
print("\nAntiVirus Check\n")
print("This may take some time")
scan("/root/files/")
