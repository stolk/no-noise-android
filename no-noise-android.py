#!/usr/bin/python

import os
import sys

argc = len( sys.argv )
if argc > 2 :
	print "Usage:", sys.argv[0],"[deviceid]"


try:
	f = open( "noisy.tags", "r" )
	g = open( "important.tags", "r")
except:
	f = None
	g = None

if not f :
	try:
		home = os.path.expanduser( "~" )
		fname = home+"/.android/noisy.tags"
		gname = home+"/.android/important.tags"
		f = open( fname, "r" )
		g = open( gname, "r" )
	except:
		print sys.argv[0], "needs files 'noisy.tags' and 'important.tags' either in ~/.android or current working directory."
		sys.exit( 1 )

lines = f.readlines()
tags = [ x.strip() for x in lines ]

implines = g.readlines()
imptags = [ x.strip() for x in implines ]

print "Read", len( tags ), "noisy tags that will be filtered."
print "Read", len( imptags), "important tags that will be emphasized."

if argc == 1 :
	cmd = "adb logcat -v brief"
else :
	cmd = "adb -s %s logcat -v brief" % ( sys.argv[1], )

os.system( cmd + " -c" )
f = os.popen( cmd, "r" )
done = False

while not done:
	try:
		line = f.readline()
		if line:
			tag = line[ 2: ].split( "(" )[ 0 ].strip()
			if not tag in tags :
				imp = tag in imptags
				if imp:
					sys.stdout.write("\033[1m" + line + "\033[m")
				else :
					sys.stdout.write(line)
		else:
			done = True
	except KeyboardInterrupt:
		done = True

f.close()
sys.exit( 0 )

