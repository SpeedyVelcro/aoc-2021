#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Pilots a submarine according to a text file of instructions, returning the product of final depth and horizontal position")
parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', help="Print extra debug info")
parser.add_argument("file", metavar="FILE", help="Text file to take instructions from")

args = parser.parse_args()
verbose = args.verbose
filename = args.file

with open(filename) as f:
	depth = 0
	horizontal = 0
	aim = 0
	for line in f:
		parts = line.split(" ")
		distance = int(parts[1])
		command = parts[0]
		if command == "forward":
			horizontal += distance
			depth += aim * distance
		elif command == "down":
			aim += distance
		elif command == "up":
			aim -= distance
	print(depth * horizontal)
