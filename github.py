from requests import request
from requests.auth import HTTPBasicAuth
from fabric.api import prompt
import json

user = None
auth = None

def get_auth():
	global auth
	global user
	if auth == None:
		user = prompt("Enter Github username:")
		passwd = prompt("Enter Github password:")
		auth = HTTPBasicAuth(user, passwd)

def api(method, url, **kwargs):
	get_auth()
	if "data" in kwargs:
		kwargs["data"] = json.dumps(kwargs["data"])
	resp = request(method, "https://api.github.com%s" % url, auth=auth, **kwargs)
	resp.raise_for_status()
	if resp.status_code != 204:
		return resp.json()

def get_key(title):
	get_auth()
	keys = api("GET", "/user/keys")
	for k in keys:
		if k["title"] == title:
			return k

	return None

def add_key(title, key):
	get_auth()
	api("POST", "/user/keys", data={ "title": title, "key": key })

