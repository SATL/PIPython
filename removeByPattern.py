import os
import fnmatch
import sys

def removeByPattern(path, pattern):
	print "Searching in "+path+" with pattern "+pattern+"\n"
	matchs = [];
	for root, dirnames, filenames in os.walk(path):
		for filename in fnmatch.filter(filenames, pattern):
			matchs.append(os.path.join(root,filename))

	for file in matchs:
		os.remove(file)	
		print file+" removed\n"

if __name__ == '__main__':
	if len(sys.argv)<3:
		print "Error command \n"
		print "Example: removeByPath 'path' 'regex' \n"

	else:
		path = sys.argv[1]
		pattern = sys.argv[2]
		removeByPattern(path, pattern)
