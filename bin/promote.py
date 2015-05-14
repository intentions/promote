#!/usr/bin/python
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

ConfigFile = "promote.json"
LogFileName = "prompte.log"

#debugFlag=True

def readConf(confFile):
    """
    reads the config file, which passes the full path
    names for the source and destination files
    """
    with open(confFile) as json_data_file:
        confData = json.load(json_data_file)

    return(confData)

def parseConf(confData):
	"""
	takes the config data and calls the moveFile function
	"""
	groupNames = confData.keys()
	for group in groupNames:
		logger.info("processing {0}".format(confData[group]["group_name"]))
		logger.info("source: {0}".format(confData[group]["source"]))
		logger.info("destination: {0}".format(confData[group]["destination"]))
		for f in confData[group]["file_names"]:
			logger.info("file name: {0}".format(f))


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
    if ( debugFlag):
        fh.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    else:
        fh.setLevel(logging.INFO)
    ch.setLevel(logging.INFO)            
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
	
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

def verifyFile(source, destination)
	"""
	uses sha512 to verify that the soruce file and the destination file are the same
	"""
	sourceHash = hashlib.sha256(open(source, 'rb').read()).digest()
	destinationHash = hashlib.sha256(open(destination, 'rb').read()).digest()
	
	if sourceHash == destinationHash:
		return True
	
	return False
	
if __name__ == "__main__":
	"""
	main function
	"""
	logger =  logConfigure(LogFileName)
	
	#read confing file
	confData = readConf(ConfigFile)
	parseConf(confData)



    


