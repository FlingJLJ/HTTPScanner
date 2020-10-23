import sys
import requests as req

wlist = ["js", "admin", "users"]

for word in wlist:
	r = req.get(f"https://{sys.argv[1]}/{word}")
	if r.status_code != 404 | r.status_code != 403:
		print(f"Page found: /{word} Status: {r.status_code}")
	if r.status_code == 403:
		print("Error: You have been denied access to this web server.")
		input("Press the ENTER key to attempt to continue.")