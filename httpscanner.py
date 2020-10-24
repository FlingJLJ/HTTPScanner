import os
import requests as req

wlist = ["js", "admin", "users", "src"]

url = input("Enter URL to scan: ")

print(f"""-- HTTPScanner --
----------------------------------
URL: {url}
----------------------------------""")

for word in wlist:
	try:
		r = req.get(f"https://{url}/{word}") # attempt to get
	except:
		print("Invalid url, press enter to exit.")
		input()
		exit()
	if r.status_code != 404 | r.status_code != 403: # remove irrelevant responses
		print(f"Found: /{word} | Status: {r.status_code}")
	if r.status_code == 403: # alert user on potential IP ban
		print("Error: You have been denied access to this web server.")
		input("Press the ENTER key to attempt to continue.")

print("Scanning done.")
input("Press any key to exit...")