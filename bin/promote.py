"""
Promotes files as directed in the config file
"""

#import modules
import logging
import json
#for file copy
import shutil
import os
#import for file verification
import hashlib

#debugFlag=True

def readConf(confFile):
	"""
	reads the config file, which passes the full path
	names for the source and destination files
	"""
	with open(confFile) as json_data_file:
		configData = json.load(json_data_file)

	return configData

def parseConf(confData):
	"""
	takes the config data and calls the moveFile function
	"""
	groupNames = confData.keys()
	for group in groupNames:
		logger.info("processing {0}".format(confData[group]["group_name"]))
		logger.info("source: {0}".format(confData[group]["source"]))
		sourcePath = confData[group]["source"]
		logger.info("destination: {0}".format(confData[group]["destination"]))
		destinationPath = confData[group]["destination"]
		for f in confData[group]["file_names"]:
			logger.info("file name: {0}".format(f))
			fileSource = "{0}/{1}".format(sourcePath, f)
			fileDestination = "{0}/{1}".format(destinationPath, f)
			moveFile(fileSource, fileDestination)
	return True

def logConfigure(logFileName, debugFlag=False):
	"""
	experimental function to configure logging
	"""
	logPath = '../log/'

	logFile = '{0}{1}'.format(logPath, logFileName)

	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)

	# create file handler which logs even debug messages
	fh = logging.FileHandler(logFile)
	fh.setLevel(logging.DEBUG)

	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.INFO)
	#set logging level
	if debugFlag:
		fh.setLevel(logging.DEBUG)
		ch.setLevel(logging.DEBUG)
	else:
		fh.setLevel(logging.INFO)
		ch.setLevel(logging.INFO)
	# create formatter and add it to the handlers
	formatOptions = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
	formatter = logging.Formatter(formatOptions)
	ch.setFormatter(formatter)
	fh.setFormatter(formatter)

	# add the handlers to logger
	logger.addHandler(ch)
	logger.addHandler(fh)

	return logger


def moveFile(src, dest, bak="bak"):
	"""
	Moves a given file from one directory to another,
	if the target file exists in that directory then
	the target is coppied as .bak
	"""
	message = "processing: {0} -> {1}".format(src, dest)
	logger.info(message)
	
	if os.path.exists(dest):
		backupFileName = "{0}.{1}".format(dest, bak)
		message = "file {0} exists, creating backup: {1}".format(dest, backupFileName)
		logger.info(message)
		try:
			shutil.move(dest, backupFileName)
		except IOError as errorMessage:
			logger.error(errorMessage)
			return False

	if os.path.exists(src):
		message = "copying {0} to {1})".format(src, dest)
		try:
			shutil.copy(src, dest)
		except IOError as errorMessage:
			logger.error(errorMessage)
			return False

	#verify that files are the same
	(fileCheck, fileSig) = verifyFile(src, dest)
	if fileCheck:
		message = "File transfer verified {0} -> {1}".format(src, dest)
		logger.info(message)
		message = "File Signature for {0}: {1}".format(src, fileSig)
		logger.info(message)
		return True
	else:
		message = "file signatures do not match, rolling back {0} -> {1}".format(backupFileName, dest)
		logger.error(message)
	
	#roll back file
	try:
		shutil.move(backupFileName, dest)
	except IOError as errorMessage:
		logger.error(errorMessage)
		return False
	

	
def checkGit(directory):
	"""
	checks to see if there are any pending git commits
	any pending commits and the script will exit
	"""

def verifyFile(source, destination):
	"""
	uses sha512 to verify that the soruce file and the destination file are
	the same
	"""
	sourceHash = hashlib.sha256(open(source, 'rb').read()).digest()
	destinationHash = hashlib.sha256(open(destination, 'rb').read()).digest()

	if sourceHash == destinationHash:
		return (True, str(sourceHash))

	return False

def test_function():
	"""
	Testing funciton for nose
	"""

	logger = logConfigure("promote_test.log")
	
	message = "starting test of promote.py"
	logger.info(message)
	testConfigFile = "test.json"
	message = "testing existence of test config file {0}".format(testConfigFile)
	logger.info(message)
	testConfigExists = False
	#try:
	#	os.path.isfile(testConfigFile)
#	except:
#		testConfigExists = False
		
	assert testConfigExists == True
#	return True
	

	
if __name__ == "__main__":
	"""
	main function
	"""
	ConfigFile = "promote.json"
	LogFileName = "prompte.log"

	logger = logConfigure(LogFileName)

	#read confing file
	confData = readConf(ConfigFile)
	parseConf(confData)
