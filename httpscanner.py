import time
import requests as req
import wordlist
import math

rawlist = wordlist.wlistraw

global wlist
wlist = rawlist.split("\n")

del rawlist

global url
url = input("Enter URL to scan: ")
try:
	req.get(f"https://{url}")
except:
	print("Invalid url, press enter to exit.")
	input()
	exit()

def scan():
	r = req.get(f"https://{url}/{word}") # attempt to get
	if r.status_code == 200: # remove irrelevant responses
		print(f"/{word}")
	if r.status_code == 403: # alert user on potential IP ban
		print("Error: You might have been denied access to this web server.")

startTime = time.time()

for i, word in enumerate(wlist):
	scan()

print(f"\nScanning done. Time elapsed: {time.time() - startTime}")
input("Press any key to exit...")