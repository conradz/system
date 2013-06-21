from utils import install, is_installed
from fabric.api import run
from fabric.contrib.files import exists
import github

def setup():
	if not is_installed("vim"):
		install("vim")

	if not exists("~/.vim"):
		github.clone("vimfiles", "~/.vim")

	if not exists("~/.vimrc"):
		run("ln ~/.vim/vimrc ~/.vimrc")

