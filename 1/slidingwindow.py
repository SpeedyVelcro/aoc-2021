#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Counts the number of times a three-measurement sliding window increases")
parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', help="Print debug information")
parser.add_argument("file", metavar="FILE", help="File containing depth measurements")

args = parser.parse_args()
verbose = args.verbose
filename = args.file

with open(filename) as f:
	increases = 0
	window = []
	previous_sum = 0
	first_window = True
	for line in f:
		if len(window) > 0:
			window.pop(0)
		window.append(int(line))
		if len(window) < 3:
			window.append(int(line))
		elif first_window:
			previous_sum = sum(window)
			first_window = False
		else:
			current_sum = sum(window)
			if current_sum > previous_sum:
				increases += 1
			previous_sum = current_sum
	print(increases)
