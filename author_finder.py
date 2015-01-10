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


#TODO normalize results/authors according to the number of patterns



def usage():
	"""
	display how to use the script
	"""
	print "usage: python " + sys.argv[0].split("/")[-1] + " [PATTERN_DIR] [SONG_DIR]"



def get_name(f):
	"""
	get the author using the file's name

	:param f: path to the pattern file
	:return: name of the matching author
	"""
	f = f.split("/")[-1]
	f = f.split(".")[0]
	result = ""

	for w in f.split("_"):
		result += w[0].upper() + w[1:] + " "

	return result[:-1]



def load_patterns(f):
	"""
	load patterns stored in a file into a python dictionary

	:param f: path to the pattern file
	:return: dictionary containing lyrics patterns
	"""
	result = {}
	pattern_file = codecs.open(f, "r", "utf-8")
	
	for l in pattern_file.readlines():
		words, sup = l.split("\t")
		words = words[1:-1]
		words = words.replace("}{", " ")
		sup = sup[4:-1]

		result[words] = sup

	return result



def normalize(patts):
    #TODO
    return None



def merge_patterns(patt1, patt2):
	"""
	merge to dictionaries (data structure used for patterns)
	if a key is in both dict, its value in the resulting dict
	will equal to patt1[key] + patt2[key]

	:param patt1: 1st pattern dictionary
	:param patt2: 2nd pattern dictionary
	:return: merged patterns (python dictionnary)
	"""
	result = patt1.copy()

	for k in patt2.keys():
		if k not in result:
			result[k] = patt2[k]
		else:
			result[k] += patt2[k]

	return result



def emerging_patterns(patt1, patt2):
	"""
	find patterns in patt1 which are not in patt2

	:param patt1: reference pattern dictionary
	:param patt2: compared dictionary
	:return: dictionary of emerging patterns
	"""
	result = {}

	for k in patt1.keys():
		if k not in patt2.keys():
			result[k] = patt1[k]

	return result



def cosine(v1, v2):
	"""
	compute the cosine distance between two dictionaries

	:param v1: 1st dictionary
	:param v2: 2nd dictionary
	:return: distance between v1 & v2
	"""
    if len(v2.keys()) == 0 or len(v1.keys() == 0):
        return 0.0

    v1v2 = 0
    v1v1 = 0
    v2v2 = 0
    for attr in set(v1.keys() + v2.keys()):
        if attr in v1:
            attr1 = v1[attr]
        else:
            attr1 = 0

        if attr in v2:
            attr2 = v2[attr]
        else:
            attr2 = 0

        v1v2 += (attr1 * attr2)
        v1v1 += (attr1 * attr1)
        v2v2 += (attr2 * attr2)
    return v1v2 / (math.sqrt(v1v1) * math.sqrt(v2v2))



def main():
	if not len(sys.argv) > 2:
		print "[ERROR] " + sys.argv[0]+" expected at least 2 arguments !"
		usage()
		sys.exit(2)

	patterns_dir = sys.argv[1]
	if not os.path.isdir(patterns_dir):
		print "[ERROR] " + sys.argv[0]+": " + patterns_dir + " is not a directory !"
		usage()
		sys.exit(2)

	song_dir = sys.argv[2]
	if not os.path.isdir(song_dir):
		print "[ERROR] " + sys.argv[0]+": " + song_dir + " is not a directory !"
		usage()
		sys.exit(2)


	patterns = {}

	# load all patterns
	for f in glob.glob(patterns_dir + "/*"):
		patterns[get_name(f)] = load_patterns(f)




if __name__ == "__main__":
	main()

