import os
import requests as req

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

wlist = ["js", "admin", "users", "src"]

clear()
url = input("Enter URL to scan: ")

clear()
print(f"""-- HTTPScanner --
----------------------------------
URL: {url}
----------------------------------""")

for word in wlist:
	try:
		r = req.get(f"https://{url}/{word}")
	except:
		print("Invalid url, press enter to exit.")
		input()
		exit()
	if r.status_code != 404 | r.status_code != 403:
		print(f"Found: /{word} | Status: {r.status_code}")
	if r.status_code == 403:
		print("Error: You have been denied access to this web server.")
		input("Press the ENTER key to attempt to continue.")

print("Scanning done.")

input()