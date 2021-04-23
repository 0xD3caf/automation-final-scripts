#Search for flag on Homepage
#Mackenzie Summers
#Run from Win10


import requests, re
def scan():
	resp = requests.get("http://10.12.0.30/index.php")
	regex_str = "CNS\{[a-fA-F0-9]{32}\}"
	flag_list = re.findall(regex_str, resp.text)
	print("Flags Found\n")
	for flag in flag_list:
		print("Flag: {}".format(flag))
print("\nHomepage Flag Scan\n")
scan()
