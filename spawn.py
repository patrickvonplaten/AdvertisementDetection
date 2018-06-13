#!/usr/bin/env python

'''
Created on 18.03.2011
@author: Christian

This is the python implementation of the original spawn script for starting jobs in the IENT queue.
It reads the spawn.cfg file and reads all the job parameters from it.
From these parameters a list of commands is generated that will be sent to the queue.
The parameters can have multiple values so that all value combinations will be submitted at once.

Sample 'spawn.cfg' file:
    # The command to run for every job
    command="run.sh"
    # The names of all the parameters for the 'command'.
    # These should also be specified in the 'dirname' and have to be specified as 'values_{parameter}'.  
    names="input param1 param2"
    # The dirname of the directory that will be created for every job. If a parameter is not specified here but
    # has multiple values as 'values_{parameter}' entry, multiple jobs will be started in a single directory.
    # If a directory for a certain parameter combination already existst no job will be submitted.
    dirname="dataTest/\${input##*/}/FirstParam\${param1}-SecondParam\${param2}-TEST"
    
    # The extra parameters for the qsub command. See the qsub wiki for possible extra parameters.
    extra_params="-p -700"
    
    # The values for the parameters. For every combination of these parameters a job will be started.  
    values_input="input/baboon input/barbara"
    values_param1="1 2 3"
    values_param2="A B C"

If this configuration is used and started in /data/feldmann/spawnTest/ the following jobs will be submitted 
and the corresponding working directories will be created:

    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam1-SecondParamA-TEST" -N "run.sh-dataTest-baboon-FirstParam1-SecondParamA-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="1" --param2="A"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam1-SecondParamB-TEST" -N "run.sh-dataTest-baboon-FirstParam1-SecondParamB-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="1" --param2="B"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam1-SecondParamC-TEST" -N "run.sh-dataTest-baboon-FirstParam1-SecondParamC-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="1" --param2="C"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam2-SecondParamA-TEST" -N "run.sh-dataTest-baboon-FirstParam2-SecondParamA-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="2" --param2="A"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam2-SecondParamB-TEST" -N "run.sh-dataTest-baboon-FirstParam2-SecondParamB-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="2" --param2="B"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam2-SecondParamC-TEST" -N "run.sh-dataTest-baboon-FirstParam2-SecondParamC-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="2" --param2="C"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam3-SecondParamA-TEST" -N "run.sh-dataTest-baboon-FirstParam3-SecondParamA-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="3" --param2="A"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam3-SecondParamB-TEST" -N "run.sh-dataTest-baboon-FirstParam3-SecondParamB-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="3" --param2="B"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/baboon/FirstParam3-SecondParamC-TEST" -N "run.sh-dataTest-baboon-FirstParam3-SecondParamC-TEST" /data/feldmann/spawnTest/run.sh --input="input/baboon" --param1="3" --param2="C"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam1-SecondParamA-TEST" -N "run.sh-dataTest-barbara-FirstParam1-SecondParamA-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="1" --param2="A"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam1-SecondParamB-TEST" -N "run.sh-dataTest-barbara-FirstParam1-SecondParamB-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="1" --param2="B"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam1-SecondParamC-TEST" -N "run.sh-dataTest-barbara-FirstParam1-SecondParamC-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="1" --param2="C"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam2-SecondParamA-TEST" -N "run.sh-dataTest-barbara-FirstParam2-SecondParamA-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="2" --param2="A"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam2-SecondParamB-TEST" -N "run.sh-dataTest-barbara-FirstParam2-SecondParamB-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="2" --param2="B"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam2-SecondParamC-TEST" -N "run.sh-dataTest-barbara-FirstParam2-SecondParamC-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="2" --param2="C"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam3-SecondParamA-TEST" -N "run.sh-dataTest-barbara-FirstParam3-SecondParamA-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="3" --param2="A"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam3-SecondParamB-TEST" -N "run.sh-dataTest-barbara-FirstParam3-SecondParamB-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="3" --param2="B"
    qsub -p -700 -wd "/data/feldmann/spawnTest/dataTest/barbara/FirstParam3-SecondParamC-TEST" -N "run.sh-dataTest-barbara-FirstParam3-SecondParamC-TEST" /data/feldmann/spawnTest/run.sh --input="input/barbara" --param1="3" --param2="C"

Sample run.sh script:
	#!/bin/bash

	for i in "$@"; do
		name="${i%%=*}"
		name="${name//-/_}"
		eval ${name#__}="${i#*=}"
	done

	# Create links and directories as needed by the actual job.
	ln -s "../../../$input" original
	mkdir reconstruction

	# Here you can start your program.
	# For example: myProgramm $input $param1 $param2
	echo $input $param1 $param2

Spawning can be controlled by some switches:

    -c (-count)      - Only prints the number of jobs that will be submitted. No directories will be created or actual jobs started.
    -d (-debug)      - prints all the submit commands that would be executed to stdout. No directories will be created or actual jobs started.
    -h (-help)       - Print the help message.
    -r (-restart)    - Jobs will also be started if the corresponding directory already exists. Files in the directory might be overwritten by the new job.
    -s (-silent)     - Hide warnings and output. Only print errors.

'''

import os
import getopt
import sys
import shutil
import subprocess

# If true no warnings or other messages will be printed. 
bSilent = False
# Warn by printing the message if bSilent is False.
def warning(message):
    if (not bSilent):
        print message
# Print the error message and exit (sys.exit(1)).
def error(message):
    print message
    sys.exit(1)
# One job represented by all its information needed for starting it.
class Job():
    def __init__(self, name, dir, command, extra_params, working_directory):
        self.name = name
        self.dir = dir
        self.command = command
        self.extra_params = extra_params
        self.working_directory = working_directory

# Ask a yes/no question.
def query_yes_no(question):
    valid = {"yes":True, "y":True, "ye":True, "no":False, "n":False}
    prompt = " [Y/n] "
    default="yes"
    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

# Returns the cartesian product of all interables in the list.
# For example product( [ [1,2,3], ['A', 'B', 'C'] ] ) returns 
# [[1, 'A'], [1, 'B'], [1, 'C'], [2, 'A'], [2, 'B'], [2, 'C'], [3, 'A'], [3, 'B'], [3, 'C']].
def product(list):
    retList = []
    if (len(list) == 1):
        for val in list[0]:
            retList.append([val])
        return retList
    param = list.pop(0)
    subCombinations = product(list)
    for val in param:
        for subcomb in subCombinations:
            retList.append([val] + subcomb)
    return retList

# Handles reading the config file and lets you iterate over its parameter/argument pairs.
# Also direct access to the parameters is possible. 
# ConfigFileHanlder[parameter] will return the agrgument for the given parameter.
# ValueError will be raised if the parameter does not exist in the config file. 
# Existance of a parameter can be tested by the in statement (if parameter in configFileHandler). 
class configFileHandler():
    def __init__(self, filename):
        self._iteratorIdx = 0
        self._paramData = []
        self._argumentData = []
        
        if (not os.path.exists(filename)):
            error("%s could not be found." % (filename))
        configFileObject = open(filename, 'r')
        
        # parse the file and save all parameters and attributes.
        for lineNr, line in enumerate(configFileObject):
            if (line[0] == '#' or line.isspace()):
                # Ignore empty lines and lines starting with '#'.
                continue
            
            # Split the line. The format is always: arg="val"
            param, arg = self._splitConfigLine( line, lineNr )
            if (param in self._paramData):
                # Parameter has already ben defined.
                error("Error in line %i. Parameter %s is defined twice." % (lineNr, param)) 
            self._paramData.append( param )
            self._argumentData.append( arg )
        
    # Split one line in the config file into parameter and argument (format: parameter="agrgument").
    def _splitConfigLine( self, line, lineNr ):
        # Search for the first '='
        lineSplit = line.split('=', 1)
        
        # Handle errors (format mismatch)
        if (len(lineSplit) > 2):
            error("Error in line %i. More than one '=' found.\nThe allowed format is: parameter=\"argument\"" % ( lineNr ))
        if (len(lineSplit) == 0):
            error("Error in line %i. No '=' found.\nThe allowed format is: parameter=\"argument\"" % ( lineNr ))
        if (lineSplit[1].count('"') > 2):
            error("Error in line %i. Too many '\"' found.\nThe allowed format is: parameter=\"argument\"" % ( lineNr ))
        if (lineSplit[1].count('"') < 2):
            error("Error in line %i. Not enough '\"' found.\nThe allowed format is: parameter=\"argument\"" % ( lineNr ))
        
        arg = lineSplit[1].strip('" \n')
        param = lineSplit[0].strip(' ')
        return param, arg
    
    # Returns if the parameter exists. Used for "in" statement.
    def __contains__(self, parameter):
        return parameter in self._paramData
    # Returns the argument for the given parameter. Used for the "[]" operator.
    def __getitem__(self, parameter):
        return self._argumentData[self._paramData.index( parameter )]
    # Return the iterable object (self). Reset iterator to 0.
    def __iter__(self):
        self._iteratorIdx = 0
        return self
    # Return the next parameter/argument pari.
    def next(self):
        self._iteratorIdx += 1
        if (self._iteratorIdx > len(self._paramData)):
            raise StopIteration
        return self._paramData[self._iteratorIdx - 1], self._argumentData[self._iteratorIdx - 1] 

# Handles the dirname string in the config file. e.g. "dataAll/\${input##*/}/Param1Val\${param1}-Param2Val\${param2}-End".
# The parameters in the form \${param} (in this example 'input', 'param1', and 'param2') are extracted and can be replaced by actual values.
# The parameters can be iterated by iterating this class (for param in dirNameHandlerInstance).
# The existance of a parameter can be tested by the in statement (if param in dirNameHandlerInstance).
# getDirForParameters finally returns a string representation of the dirname with the parameters replaced by actual values.
# For our example the call dirNameHandlerInstance.getDirForParameters( ['input', 'param1', 'param2'], ['baboon', '5', '6'] ) will return
# "dataAll/baboon/Param1Val5-Param2Val6-End".
class dirNameHandler():
    # Splits the dir string into peaces that are put into self.__splitPath and self._splitParams.
    # For example the string "dataAll/\${input##*/}/Param1Val\${param1}-Param2Val\${param2}-End"
    # will be split into: self._splitPath=["dataAll/", "/Param1Val", "-Param2Val", "-End"]
    # and self._splitParams=["input", "param1", "param2"].
    # The path can then be constructed by taking self._splitPath[0] + the value for self._splitParams[0] and so on.
    def __init__(self, dirString):
        self._splitParams = []
        self._splitPath = []
        self._iteratorIdx = 0
        searchIdx = 0
        paramEnd = 0
        while (True):
            paramStart = dirString.find('\${', searchIdx)
            if (paramStart == -1):
                break
            paramEnd = dirString.find('}', paramStart)
            param = dirString[paramStart+3: paramEnd]
            if (param[-4:] == '##*/'):
                param = param[:-4]
            
            self._splitPath.append( dirString[searchIdx:paramStart] )
            self._splitParams.append( param )
            searchIdx = paramEnd + 1
        self._splitPath.append( dirString[paramEnd+1:] )
    
    # Returns the path where all the parameters in paramList are replaced by the corresponding values in valueList.
    # If the 'input' parameter contains a path with subdirectories (e.g. 'input/baboon') only the last part ('baboon') will
    # be inserted into the dirname string.
	# Example: The dirname is "dataAll/\${input##*/}/Param1Val\${param1}-Param2Val\${param2}-End", the paramList is
	# ['input', 'param1', 'param2'] and valueList is ['baboon', '23', '33']. The returned string will be:
	# "dataAll/baboon/Param1Val23-Param2Val33-End".
    def getDirForParameters(self, paramList, valueList):
        assert (len(paramList) == len(valueList))
        assert (len(paramList) >= len(self._splitParams))
        dirString = ""
        for idx, param in enumerate(self):
            arg = valueList[paramList.index( param )]
            if (param == "input"):
                arg = arg.split('/')[-1]
            dirString += self._splitPath[idx] + arg
        return dirString + self._splitPath[-1]
    # Returns if the parameter exists in the path (\${parameter}. Used for "in" statement.
    def __contains__(self, parameter):
        return parameter in self._splitParams
    # Return the iterable object (self). Reset iterator to 0.
    def __iter__(self):
        self._iteratorIdx = 0
        return self
    # Return the next parameter.
    def next(self):
        self._iteratorIdx += 1
        if (self._iteratorIdx > len(self._splitParams)):
            raise StopIteration
        return self._splitParams[self._iteratorIdx - 1] 

# Handles the jobs for the config file spawn.cfg.
# On construction the spawn.cfg file will be opened, parsed, and checked for errors.
# Jobs are then started with startJobs.
class jobsHandler():
    def __init__(self):
        # Open the config file
        self._cfgFile = configFileHandler('spawn.cfg')
        
        if (not 'command' in self._cfgFile or self._cfgFile['command'] == ""):
            error("Error parsing config file. No 'command' parameter given.")
        if (not 'names' in self._cfgFile or self._cfgFile['names'] == ""):
            error("Error parsing config file. No 'names' parameter given.")
        if (not 'dirname' in self._cfgFile or self._cfgFile['dirname'] == ""):
            error("Error parsing config file. No 'dirname' parameter given.")
        
        # Check if all the values defined in names have been defined with a "values_name" parameter.
        # This will only generate warnings since we don't need the names list for parsing the config file.
        namesList = self._cfgFile['names'].split()
        for name in namesList:
            if (not ("values_" + name) in self._cfgFile):
                warning("Warning in cfg file. No value for the given parameter %s (values_%s)" % (name, name))
        for parameter, _ in self._cfgFile:
            if (parameter[:7] == "values_"):
                if (not parameter[7:] in namesList):
                    warning("Warning in cfg file. The value %s (%s) has not been defined in names." % (parameter[7:], parameter))
        
        # Split dirname
        self._dirname = dirNameHandler( self._cfgFile['dirname'] )
            
        # Check if all the values_* parameters have values and are all specified in dirname.
        for parameter, arg in self._cfgFile:
            if (parameter[:7] == 'values'):
                if (parameter[7:] not in self._dirname):
                    warning("Warning: The parameter %s (%s) is not specified in dirname." % (parameter[:7], parameter))
                    if (len(arg) > 1):
                        warning("Warning: The argument for parameter %s (%s) has multiple entries. This will start more than one job in one directory." % (parameter[:7], parameter))
        
        # Check if all the parameters in dirName have one ore more arguments ('values_parameter').
        for parameter in self._dirname:
            if (not ('values_'+parameter) in self._cfgFile):
                error("The parameter %s (%s) has been specified in the dirname but has no config entry." % (parameter, 'values_'+parameter))
            if (len(self._cfgFile['values_'+parameter]) == 0):
                error("The parameter %s (%s) has been specified in the dirname but has an empty config entry (No argument(s))." % (parameter, 'values_'+parameter))
            
    # Get the number of jobs that will be started by this config.
    def getJobCount(self, bRestart):
        nrJobs = 0
        jobsList = self._getJobList()
        
        for job in jobsList:
            # Check if the directory for the job exists.
            if (os.path.exists(job.dir) and not bRestart):
                continue            
            nrJobs += 1
        return nrJobs
    
    # Send the given command to bash and execute it.
    def _executeCommand(self, command, silent=False):
        # Submit job
        try:
            if (silent):
                retcode = subprocess.call(command, shell=True, stdout=subprocess.PIPE)
            else:
                retcode = subprocess.call(command, shell=True)
            if retcode < 0:
                print >> sys.stderr, "Child was terminated by signal", -retcode
            else:
                if (retcode != 0):
                    print >> sys.stderr, "Child returned", retcode
        except OSError, e:
            print >> sys.stderr, "Execution failed:", e
    
    # Returns a list containing all the jobs that are defined by the config file.
    def _getJobList(self):
        jobsList = []
        
        parametersList = []
        argumentsList = []
        for param, arg in self._cfgFile:
            if (param[:7] == 'values_'):
                parametersList.append( param[7:] )
                argumentsList.append( arg.split() )
        
        allArgumentCombinations = product( argumentsList )
        command = self._cfgFile['command']
        jobExtraParams = self._cfgFile['extra_params']
        
        for parameterArgumentCombination in allArgumentCombinations:
            jobDir = self._dirname.getDirForParameters(parametersList, parameterArgumentCombination)
            jobName = command + '-' + jobDir.replace('/', '-')
            jobWorkingDir = os.getcwd() + "/" + jobDir
            jobCommand = os.getcwd() + "/" + command + ""
            for param, arg in zip(parametersList, parameterArgumentCombination):
                jobCommand += " --%s=%s" % (param, arg)
            
            jobsList.append( Job(jobName, jobDir, jobCommand, jobExtraParams, jobWorkingDir) )
        
        return jobsList
    
    # Starts all the jobs. If debug mode is on the submit commands will only be printed to std. No jobs will be actually started.
    # If bRestart is True the job will also be started if the directory of the job already exists.
    def startJobs(self, debugMode=False, bRestart=False):
        nrJobs = 0
        jobsList = self._getJobList()
        
        for job in jobsList:
            # Check if the directory for the job exists.
            if (os.path.exists(job.dir) and not bRestart):
                continue
            
            submitCommand = "qsub %s -wd \"%s\" -N \"%s\" %s" % (job.extra_params, job.working_directory, job.name, job.command)            
            nrJobs += 1
            
            if (debugMode and not bSilent):
                print submitCommand
            else:
                # Create directory if it doesn't exist.
                if (not os.path.exists(job.dir)):
                    os.makedirs(job.dir)
                # Start job
                self._executeCommand(submitCommand, bSilent)
        
        if (not bSilent):
            print "%i jobs submitted." % nrJobs
        # Copy the used config file to the subdirectory
        if (os.path.exists('./' + self._cfgFile['dirname'].split('/')[0] + "/") and os.path.exists('spawn.cfg')):
            shutil.copy( 'spawn.cfg', './' + self._cfgFile['dirname'].split('/')[0] )
    
def printUsage():
    print "Reads the spawn.cfg file and starts jobs."
    print " -c (-count)      - Only prints the number of jobs that will be submitted."
    print " -d (-debug)      - prints all the submit commands that would be executed to stdout. No jobs are actually submitted."
    print " -h (-help)       - prints this help dialog."
    print " -r (-restart)    - Jobs will also be started if the corresponding directory already exists."
    print " -s (-silent)     - Hide warnings and output. Only print errors."

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt( sys.argv[1:], "dsrch", [ "debug", "silent", "restart", "count", "help"] )
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        printUsage()
        sys.exit(2)
        
    bDebugMode = False
    bRestart = False
    bPrintNrJobs = False
    for o, a in opts:
        if o in ("-h", "--help"):
            printUsage()
            sys.exit()
        elif o in ("-d", "-debug"):
            bDebugMode = True
        elif o in ("-s", "-silent"):
            bSilent = True
        elif o in ("-r", "-restart"):
            bRestart = True
        elif o in ("-c", "-count"):
            bPrintNrJobs = True
        else:
            assert False, "Unhandled command line option"
    
    handler = jobsHandler()
    nrJobs = handler.getJobCount(bRestart)
    if (bPrintNrJobs):
        print "Nr of jobs: %i" % nrJobs
    else:
        if (nrJobs > 1000 and not bDebugMode):
            # Ask if the user intended this.
            if (not query_yes_no("You are about to submit %i jobs. Are you sure?" %  nrJobs)):
                sys.exit(0)
        handler.startJobs( bDebugMode, bRestart )
    
