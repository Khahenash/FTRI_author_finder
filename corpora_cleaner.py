#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
	Carl Goubeau

:Date:
	2014/12/08 (creation)
	2015/01/05 (last update)
"""

import sys
import os
import codecs
import glob
import math
import re




def usage():
	"""
	display how to use the script
	"""
	print "\tusage: python " + sys.argv[0].split("/")[-1] + " [CORPORA]"
	print "\t[CORPORA] can be a file or a directory"



def clean(f, sw):
	file_obj = codecs.open(f, "r", "utf-8")
	string = file_obj.read()
	file_obj.close()

	string = string.replace("(", "")
	string = string.replace(")", "")
	string = re.sub("\[.*?\]", "", string)
	string = string.replace("\r", "\n")
	string = string.lower()

	#TODO stopwords

	res = codecs.open(f + ".cln", "w", "utf-8")

	for l in string.split("\n"):
		if l.strip() != "":
			res.write(l.strip())
			if l.strip()[-1] not in ["!", "?", ".", ",", ":", ";"]:
				res.write(".")
			res.write("\n")

	res.close()



def loaddata(file_path):
    """
    :param file_path: file to load
    :return: list containing each line as element
    """
    data = []
    if not os.path.isfile(file_path):
        print "[ERROR] " + file_path +": data file not found !"
        usage()
        sys.exit(2)
    print "Loading data file [" + file_path + "] ...",#
		
    for e in codecs.open(file_path, "r", "utf-8").readlines():
        data.append(e.replace("\n", ""))
    print "[DONE]"

    return data



def main():
	if not len(sys.argv) > 1:
		print "[ERROR] " + sys.argv[0]+" expected at least 1 argument !"
		usage()
		sys.exit(2)

	if os.path.isdir(sys.argv[1]):
		sw = loaddata("data/resources/english_stopwords.lst")
		for f in glob.glob(sys.argv[1] + "/*"):
			clean(f, sw)
	elif os.path.isfile(sys.argv[1]):
		clean(sys.argv[1], loaddata("data/resources/english_stopwords.lst"))
	else:
		print "[ERROR] " + sys.argv[0]+": " + sys.argv[1] + " is not a directory/file !"
		usage()
		sys.exit(2)






if __name__ == "__main__":
	main()

