#!/usr/bin/python
"""
Promotes files as directed in the config file
"""

#import modules
import logging
#for file copy
import shutil

logPath = '../log/'

logFile = logPath + 'prompte.log'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler(logFile)
fileHandler.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)

consoleFormat = '%(levelname) - %(name)s: %(message)s'
consoleFormatter = logging.Formatter(fmt=consoleFormat)
consoleHandler.setFormatter(consoleFormatter)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

def moveFile(src, dest, bak=".bak"):
	"""
	Moves a given file from one directory to another,
	if the target file exists in that directory then
	the target is coppied as .bak
	"""

def checkGit(directory):
	"""
	checks to see if there are any pending git commits
	any pending commits and the script will exit
	"""


if __name__ == "__main__":
	"""
	main function
	"""
