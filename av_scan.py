#Anitvuris / Malware Test
#Mackenzie Summers
 
import requests, hashlib, time, os, paramiko
from time import sleep
 
def scan(dir):
	client = paramiko.SSHClient()															#CHECK STARTS HERE
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect("10.12.0.30", username="root", password="password")
	os.mkdir("client_files")
	sftp = ssh.open_sftp()
	sftp.chdir(dir)
	for num in range(51):
		if num >= 9:
			curr_malware = "Malware0" + num
		else:
			curr_malware = "Malware" + num
		sftp.get("/root/files/" + curr_malware, "C:Users\\student\\Desktop\\scripts")		#CHECK
 	sftp.close()
	client.close()
	API_KEY = "ad339e729d83f12a897462dd0ccbd9e193b5e7cb1e12b8045a6cc877afa5d7b3"
	url = 'https://www.virustotal.com/vtapi/v2/file/scan'
	os.chdir("scripts")
	file_list = os.listdir()																#CHECK STOPS HERE
	for file in file_list:
		files = ({'file': (file, open(file,'rb'))})
		try:
			response = requests.post(url, files=files, params={'apikey': API_KEY})
			response_data = response.json()
			resource = response_data.get("resource")
		except:
			print("looks like this file didnt work")
		url = 'https://www.virustotal.com/vtapi/v2/file/report'
		for i in range(6):	
			try:
				resp = requests.get(url, params={'apikey': API_KEY, 'resource': resource})
				print(resp.json())
				resp = resp.json()
				break
			except:
				sleep(5)
				continue
		total_checked = resp.get("total") 
		hits = resp.get("positives")
		if hits == 0:
			percent = 0
		else:
			percent = total_checked/hits
		if percent >= .05:
			print("MALWARE FOUND")
			print("File: {} is Malware".format(file))
			break
		else:
			sleep(12)
 
print("\nAntiVirus Check\n")
print("This may take some time")
scan("/root/files/")
