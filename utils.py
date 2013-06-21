from fabric.api import run, sudo, get
from StringIO import StringIO

def install(app):
	sudo("apt-get install %s -q -y" % app)

def is_installed(app):
	result = run("which %s" % app, quiet=True)
	return result.succeeded

def cat(file):
	output = StringIO()
	get(file, output)
	return output.getvalue()

