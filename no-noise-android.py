#!/usr/bin/python

import os
import sys

argc = len( sys.argv )
if argc > 2 :
	print "Usage:", sys.argv[0],"[deviceid]"


try:
	f = open( "noisy.tags", "r" )
except:
	f = None

if not f :
	try:
		home = os.path.expanduser( "~" )
		fname = home+"/.android/noisy.tags"
		print fname
		f = open( fname, "r" )
	except:
		print sys.argv[0], "needs a file 'noisy.tags' either in ~/.android or current working directory."
		sys.exit( 1 )

lines = f.readlines()
tags = [ x.strip() for x in lines ]

print "Read", len( tags ), "noisy tags that will be filtered."

if argc == 1 :
	cmd = "adb logcat"
else :
	cmd = "adb -s %s logcat" % ( sys.argv[1], )

f = os.popen( cmd, "r" )
done = False

while not done:
	try:
		line = f.readline()
		if line:
			tag = line[ 2: ].split( "(" )[ 0 ].strip()
			if not tag in tags :
				print line,
		else:
			done = True
	except KeyboardInterrupt:
		done = True

f.close()
sys.exit( 0 )

