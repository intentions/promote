#!/usr/bin/python
"""
Promotes files as directed in the config file
"""

#import modules
import logging
#for file copy
import shutil
import os

ConfigFile = ""
LogFileName = "prompte.log"

#DebugFlag=True

def readConf(confFile):
	"""
	reads the config file, which passes the full path
	names for the source and destination files
	"""

def logConfigure(logFileName, debugFlag=False):
	"""
	experimental function to configure logging
	"""

	logPath = '../log/'

	logFile = '{0}{1}'.format(logPath, logFileName)

	logger = logging.getLogger(__name__)

	if debugFlag == True:
		logger.setLevel(logging.DEBUG)
		message = "debugging enabled"
	else:
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

	logger.debug(message)

	return(logger)


def moveFile(src, dest, bak=".bak"):
	"""
	Moves a given file from one directory to another,
	if the target file exists in that directory then
	the target is coppied as .bak
	"""

	if ( os.path.exists(dest)):
		message = "file {0} exists, appending with {1}".format(dest, bak) 
		logger.info(message)
		backupFileName = "{0}.{1}".format(dest, bak)
		try:
			shutil.move(dest, backupFileName)
		except IOError as errorMessage:
			logger.error(errorMessage)
			return False

	if ( os.path.exists(src)):
		message = "copying {0} to {1)".format(src, dest)
		try:
			shutil.copy(src, dest)
		except IOError as errorMessage:
			logger.error(errorMessage)
			return False
		

def checkGit(directory):
	"""
	checks to see if there are any pending git commits
	any pending commits and the script will exit
	"""


if __name__ == "__main__":
	"""
	main function
	"""

	readConf