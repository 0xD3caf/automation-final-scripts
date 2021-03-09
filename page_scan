import requests, re, os, urllib.request, base64, binascii
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup


def capture():
    url = "https://github.com/bensooter/URLchecker/blob/master/top-1000-websites.txt"
    final_urls = []
    response = requests.get(url)
    regex_str = "\w+.[\w]*.?[a-zA-Z]$"
    soup = BeautifulSoup(response.text, "html.parser")
    test = soup.findAll(text = re.compile("(www\.)?\w*\.(\w+\.)?[a-zA-Z]+$"))
    
    counter = 0
    for val in test:
    	if counter == 0:
    		counter += 1
	 	# I added this line here to remove the instance of top-100-websites.txt from beautiful soup.
	    # It appears like it incorrectly handles the "-" character as part of a string and matches it when it should not
	    # this part would not be neccesary on other web sites.
    	elif counter > 11:
    		break
    	else:
    		final_urls.append(val)
    		counter += 1
    print("The Top 10 URLs are")
    for url in final_urls:
    	print(url)
    print("")
    print("Screenshots of each sites mainpage are avaliable in the screenshots folder created wherever this program ran\n")
    browser = webdriver.Firefox()
    current_dir = os.getcwd()
    screens_folder_path = current_dir + "/screenshots/"
    try:
    	os.mkdir(screens_folder_path)
    except:
    	pass
    for item in final_urls:
    	image_name = screens_folder_path + item + ".png"
    	site_url = "https://www." + str(item)
    	try:
    		browser.get(site_url)
    		sleep(1)
    		browser.save_screenshot(image_name)
    	except:
    		print("Unable to connect to {} - an error occured".format(item))

    browser.quit()
print("\nQuestion 1\n")
capture()
