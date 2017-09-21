#! /usr/bin/python
from Chempy.score_function import CV_bash
import sys
index = int(sys.argv[1]) # Beta index


if index == 1:
	print('UPDATE NEURAL NETWORK')

print('Starting process %d' %(index+1))
CV_bash(index)

if index == 19:
	print('Stitching together')
	from Chempy.score_function import CV_stitch
	CV_stitch()
	print('Complete')
