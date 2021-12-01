#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Counts the number of times the depth measurement increases")
parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', help="Print debug information")
parser.add_argument("file", metavar="FILE", help="File containing depth measurements")

args = parser.parse_args()
verbose = args.verbose
filename = args.file

with open(filename) as f:
	first = True
	previous = 0
	increases = 0
	for line in f:
		if first:
			first = False
			previous = int(line)
			if verbose:
				print("%d (N/A - no previous measurement)" % previous)
		else:
			current = int(line)
			if current > previous:
				increases += 1
				if verbose:
					print("%d (increased)" % current)
			elif verbose:
				print("%d (decreased)" % current)
			previous = current
	print(increases)
