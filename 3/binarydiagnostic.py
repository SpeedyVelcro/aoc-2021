#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Solves day 3, star 1 of Advent of Code 2021 for a given file input")
parser.add_argument("file", metavar="FILE", help="File to parse input from")
parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', help="Print debug info")
args = parser.parse_args()
filename = args.file
verbose = args.verbose

def bin_to_num(binary):
	# Converts binary (array of true/false) to decimal number
	binary.reverse()
	result = 0
	i = 0
	for b in binary:
		if b:
			result += 2**i
		i += 1
	return result

def main():
	with open(filename) as f:
		sums = [0] * 24
		gamma_bin = [False] * 24
		epsilon_bin = [False] * 24
		for line in f:
			i = 0
			line = list(line)
			line.reverse()
			for char in line:
				if char == "1":
					sums[i] += 1
					i += 1
				elif char == "0":
					sums[i] -= 1
					i += 1
		sums.reverse()
		if verbose:
			print("Sums are " + str(sums))
		for i in range(len(sums)):
			gamma_bin[i] = sums[i] > 0
			epsilon_bin[i] = sums[i] < 0
		if verbose:
			print("gamma: " + str(gamma_bin) + ", epsilon: " + str(epsilon_bin))
		gamma = bin_to_num(gamma_bin)
		epsilon = bin_to_num(epsilon_bin)
		if verbose:
			print("gamma: " + str(gamma) + ", epsilon: " + str(epsilon))
		print(gamma * epsilon)
		

if __name__ == "__main__":
	main()
