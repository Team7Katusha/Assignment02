'''
Created on Oct 19, 2016

@author: team_7
'''
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases

import sys, optparse

# path to the file with the description of environment variables
ENV_FILE = "local.properties"

# get the dictionary of the environment variables
env_dict = getLocalEnv(ENV_FILE)
# exit if file with environment variables wasn't found
if env_dict == -1:
    sys.exit("Failed to load environment variables")  

# get the log file handle
try:
    log = getLog(env_dict['log_dir'],sys.argv[0])
except KeyError as e:
    # exit if env_dict has no 'log_dir' location
    sys.exit("Failed to open or create log file. It's location is not found in \'local.properties\' file. Please describe it as \'log_dir\'")
# exit if log creation failed
if log == -1:
    sys.exit("Failed to open or create log file")
else:
    qaPrint(log, 'Running %s script' % sys.argv[0])    


###################################
# Process command-line arguments
###################################

for arg in sys.argv[1:]:
    # Show help
    if arg.lower() == '--help' or arg.lower() == '-h':
        qaPrint(log, 'Showing help message\n' + 
                'Usage: %s [option]\n' % sys.argv[0] +
                '\n' +
                '--help -h\t\tshow help\n' +
                '--testrun=<test_ID>\tid number of running test scenario ([0;10000])')
        sys.exit()  
    # Process 'testrun' option
    elif '--testrun=' in arg.lower():
        # Save value of 'testrun' option in trid var
        trid = arg.split('=')[1]
        # Save trid as int
        try:
            trid = int(trid)
        except Exception as e:
            qaPrint(log, str(e))
            qaPrint(log, 'Provide integer value for \'--testrun\' option. See Help for details')
            sys.exit()
        # Check if 'testrun' (trid) is in range [0;10000]
        if trid >= 0 and trid <= 10000:
            pass
        else:
            qaPrint(log, 'value of --testrun option should be in the range of [0;10000].')
            sys.exit()
    else:
        qaPrint(log, 'Unexpected argument. See Help for details')
        sys.exit()
    

###################################
# Loading test cases
###################################

qaPrint(log, 'Loading test scenario_id=%s.' % trid)
# get the dictionary of test cases from test scenario id = 'trid'
test_case = getTestCases(trid)
# exit if file with test cases wasn't found
if test_case == -1:
    qaPrint(log, 'Failed to load test scenario_id=%s.' % trid)
    sys.exit()
else:
    qaPrint(log, 'Scenario_id=%s successfully loaded.' % trid)    

qaPrint(log, str(test_case)) # STRING SHOULD BE REMOVED LATER


###################################
# Closing log file
###################################

if not log.closed:
    qaPrint(log, 'Closing log.')
    log.close()
                
