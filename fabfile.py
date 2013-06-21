from fabric.api import run, cd, sudo, get, prompt
from fabric.contrib.files import exists
from StringIO import StringIO
import github

def install(app):
	sudo("apt-get install %s -q -y" % app)

def is_installed(app):
	result = run("which %s" % app, quiet=True)
	return result.succeeded

def git():
	if not is_installed("git"):
		install("git")
	name = run("git config --global user.name", quiet=True)
	if name.failed:
		name = prompt("Enter Git name:")
		run("git config --global user.name %s" % name)

	email = run("git config --global user.email", quiet=True)
	if email.failed:
		email = prompt("Enter Git email:")
		run("git config --global user.email %s" % email)

def ssh_key():
	if not exists("~/.ssh/id_rsa"):
		run("ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ''")

def get_ssh():
	output = StringIO()
	get("~/.ssh/id_rsa.pub", output)
	return output.getvalue().strip()

def github_ssh():
	ssh_key()
	host = run("hostname").strip()
	if github.get_key(host) == None:
		github.add_key(host, get_ssh())

def clone(repo, dir=""):
	run("git clone %s %s" % (repo, dir))

def vim():
	if not is_installed("vim"):
		install("vim")

	if not exists("~/.vim"):
		git()
		github_ssh()
		clone("git@github.com:%s/vimfiles.git" % github.user, "~/.vim")

	if not exists("~/.vimrc"):
		run("ln ~/.vim/vimrc ~/.vimrc")

