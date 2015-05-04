#!/usr/bin/python
"""
Promotes files as directed in the config file
"""

#import modules
import logging
import shutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

filehandler = logging.FileHandler('../log/promote.log')
filehandler.setLevel(logging.INFO)

consolehandler = logging.StreamHandler()
consolehandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s %(name)s - %(message)s'

def moveFile(src, dest):
	"""
	Moves a given file from one directory to another
	"""

def checkGit(directory):
	"""
	checks to see if there are any pending git commits
	any pending commits and the script will exit
	"""


