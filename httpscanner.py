import math
import wordlist
import requests as req

rawlist = wordlist.wlistraw

global wlist
wlist = rawlist.split("\n")

global url
url = input("Enter URL to scan: ")

print(f"""----------------------------------
URL: {url}
----------------------------------""")

for i, word in enumerate(wlist):
	try:
		r = req.get(f"https://{url}/{word}") # attempt to get
	except:
		print("Invalid url, press enter to exit.")
		input()
		exit()
	if r.status_code != 404 | r.status_code != 403: # remove irrelevant responses
		print(f"Found: /{word} | Status: {r.status_code}; Progress: {math.floor((i / len(wlist)) * 100)}%")
	if r.status_code == 403: # alert user on potential IP ban
		print("Error: You have been denied access to this web server.")
		input("Press the ENTER key to attempt to continue.")

print("\nScanning done.")
input("Press any key to exit...")