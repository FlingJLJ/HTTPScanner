import requests as req
import threading

wlist = ["js", "admin", "users", "src"]
url = input("Enter URL to scan: ")

global found
found = 0

def scan(word, url):
	r = req.get(f"https://{url}/{word}")
	if len(r.history) > 1:
		return
	if r.status_code != 404 | r.status_code != 403:
		print(f"Page found: /{word} Status: {r.status_code}")
		found += 1
	if r.status_code == 403:
		print("Error: You have been denied access to this web server.")
		input("Press the ENTER key to attempt to continue.")

print(f"""
-- HTTPScanner --
----------------------------------
URL: {url}
----------------------------------
""")

for word in wlist:
	threading.Thread(target=scan(word, url))

if found == 0:
	print("Nothing found. :'(")

input()