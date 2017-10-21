#!/usr/local/bin/python
from ConfigParser import SafeConfigParser
import os
import sh
import sys
import os
import socket

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
    	return False
    except socket.gaierror:
    	return False

IS_CONNECTED = is_connected()

s3 = sh.aws.bake("s3")
S3_BUCKET = "s3://earthporn-images"
fullPath = os.path.realpath(__file__)
fullDirectory, filename =  os.path.split(fullPath)
DATA_DIR = os.path.join(fullDirectory, "images")

if os.path.isdir(DATA_DIR) is False:
	os.makedirs(DATA_DIR)

def validate():
	if S3_BUCKET is None:
		print "S3_BUCKET not specified in configuration. Can not perform operation."
		return False
	if IS_CONNECTED is False:
		return False
	return True

def upsync():
	if validate():
		s3("sync",DATA_DIR,S3_BUCKET,"--acl", "public-read-write")

def downsync():
	if validate():
		s3("sync",S3_BUCKET,DATA_DIR,"--acl", "public-read-write")

def main():
	if len(sys.argv) != 2:
		print "Invalid/Insufficient arguments"
	else:
		globals()[sys.argv[1]]()

if __name__ == '__main__':
    main()