from fabric.api import run
from fabric.contrib.files import exists
from utils import cat

_key = None

def setup():
	global _key
	if not exists("~/.ssh/id_rsa"):
		run("ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ''")
		_key = None

def key():
	global _key
	if _key == None:
		_key = cat("~/.ssh/id_rsa.pub")
	return _key

