import requests as req
import wordlist
import math

rawlist = wordlist.wlistraw

global wlist
wlist = rawlist.split("\n")

del rawlist

global url
url = input("Enter URL to scan: ")

def scan():
	try:
		r = req.get(f"https://{url}/{word}") # attempt to get
	except:
		print("Invalid url, press enter to exit.")
		input()
		exit()
	if r.status_code != 404 | r.status_code != 403: # remove irrelevant responses
		print(f"/{word} | Status: {r.status_code} | Progress: {math.floor((i / len(wlist)) * 100)}%")
	if r.status_code == 403: # alert user on potential IP ban
		print("Error: You may have been denied access to this web server.")
		input("Press the ENTER key to attempt to continue.")

for i, word in enumerate(wlist):
	scan()

print("\nScanning done.")
input("Press any key to exit...")