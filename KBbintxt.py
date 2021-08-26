#!/usr/bin/env python3

##@file KBbintxt.py
#  @ingroup util
#	A script for converting 256-byte raw .bin files to a txt format compatible with
#	serial input in the KENBAK-unio firmware (used in the adwaterandstir.com emulator
#	kit.
#
#	Usage: 
#	>>>KBbintxt.py [-h] <infile>
#	
#	@param infile		The file to convert.
#	@param pst			"-p n", sets the initial program counter to n [optional]
#	@param version		"-v", returns version number
#	
#	@author Robert Gallup	2021
#
#	Author:    Robert Gallup (bg@robertgallup.com)
#	License:   MIT Opensource License
#
#	Copyright 2016-2021 Robert Gallup 
#

import sys, array, os, textwrap, argparse

class DEFAULTS(object):
	VERSION = '1.0.0'

def main ():

	# Default parameters
	infile = ""
	tablewidth = 16
	version = False

	# Set up parser and handle arguments
	parser = argparse.ArgumentParser()
	parser.add_argument ("infile", help="The BMP file(s) to convert", type=argparse.FileType('r'), nargs='*', default=['-'])
	parser.add_argument ("-p", "--pgm_start", help="Sets initial program counter to \"n\",  (default: 4)", metavar="n", default=4)
	parser.add_argument ("-r", "--raw", help="Outputs data without the filename header", action="store_false")
	parser.add_argument ("-v", "--version", help="Returns the current bmp2hex version", action="store_true")
	args = parser.parse_args()

	# Options
	program_start = args.pgm_start

	if args.version:
		print ('version ' + DEFAULTS.VERSION)

	# Do the work
	for f in args.infile:
		if f == '-':
			sys.exit()
		else:
			if args.raw == True:
				print("\n" + f.name)
			bin2txt(f.name, tablewidth, program_start)

# Main conversion function
def bin2txt(infile, tablewidth, program_counter):
	# Convert tablewidth to octal/hex characters
	tablewidth = int(tablewidth) * 4

	# Initilize output buffer
	outstring =  ''

	# Open File
	fin = open(os.path.expanduser(infile), "rb")
	uint8_tstoread = os.path.getsize(os.path.expanduser(infile))
	valuesfromfile = array.array('B')
	try:
		valuesfromfile.fromfile(fin, uint8_tstoread)
	finally:
		fin.close()

	# Get bytes from file
	values=valuesfromfile.tolist()

	# Set initial program counter (only if original is zero)
	if values[3] == 0:
		values[3] = int(program_counter)

	# Generate bytes for data in output buffer
	try:
		for v in values:
			outstring += ("{0:#05o}".format(v) + ",")[2:]

	# Wrap the output buffer. Print. Then, finish.
	finally:
		outstring = textwrap.fill(outstring, tablewidth)
		print (outstring)

# Only run if launched from command line
if __name__ == '__main__': main()
