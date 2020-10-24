import pdb
import os
import requests as req
import tkMessageBox

wlist = ["js", "admin", "users", "src"]
url = input("Enter URL to scan: ")

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def fatalErr(message):
	tkMessageBox.showinfo(f"Error in {__file__.name}", f"A fatal error occured and the program must be stopped.\nError message:\n{message}")

print(f"""-- HTTPScanner --
----------------------------------
URL: {url}
----------------------------------""")

for word in wlist:
	try:
		r = req.get(f"https://{url}/{word}")
	except:
		fatalErr("Invalid URL requested.")
	if r.status_code != 404 | r.status_code != 403:
		print(f"Found: /{word} | Status: {r.status_code}")
	if r.status_code == 403:
		print("Error: You have been denied access to this web server.")
		input("Press the ENTER key to attempt to continue.")

print("Scanning done.")

input()
breakpoint()