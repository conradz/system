from fabric.api import run
from utils import install, is_installed

def get_config(name):
	result = run("git config --global %s" % name, quiet=True)
	if result.failed:
		return None
	return result

def set_config(name):
	run("git config --global %s %s" % (name, value))

def clone(repo, dir=""):
	run("git clone %s %s" % (repo, dir))

def setup():
	if not is_installed("git"):
		install("git")

	if get_config("user.name") == None:
		set_config("user.name", prompt("Enter Git username:"))
	if get_config("user.email") == None:
		set_config("user.email", prompt("Enter Git email:"))

