import sys
from Logger import Logger
for i in range(1, len(sys.argv)):
    print ("param", i, sys.argv[i])
logger = Logger(logName=sys.argv[1],modelName=sys.argv[2],logLevel=sys.argv[3],logger=sys.argv[4])