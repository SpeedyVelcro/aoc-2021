#!/usr/bin/env python3
import argparse
from numpy import * # For deep array copy

parser = argparse.ArgumentParser(description="Calculates answers to Advent of Code 2021 day 3 star 2")
parser.add_argument("file", metavar="FILE", help="File containing input")
parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', help="Print extra debug info")
args = parser.parse_args()
filename = args.file
verbose = args.verbose

def print_data_head(data):
	i = 0
	for line in data:
		print(line)
		i += 1
		if i >= 5:
			break

def parse_file(f):
	data = []
	for line in f:
		line_data = []
		line = list(line)
		for char in line:
			if char == '0':
				line_data.append(False)
			elif char == '1':
				line_data.append(True)
		data.append(line_data)
	if verbose:
		print("Parsed File. Fil head is:\n")
		print_data_head(data)
	return data

def select_oxygen_rating(data):
	bit_to_check = 0
	while len(data) > 1:
		bit_sum = 0
		for value in data:
			if value[bit_to_check]:
				bit_sum += 1
			else:
				bit_sum -= 1
		select_bit = bit_sum >= 0
		for i in range(len(data)-1, -1, -1):
			if data[i][bit_to_check] == (not select_bit):
				data.pop(i)
		bit_to_check += 1
	return data[0]

def select_co2_rating(data):
	bit_to_check = 0
	while len(data) > 1:
		bit_sum = 0
		for value in data:
			if value[bit_to_check]:
				bit_sum += 1
			else:
				bit_sum -= 1
		select_bit = bit_sum < 0
		for i in range(len(data)-1, -1, -1):
			if data[i][bit_to_check] == (not select_bit):
				data.pop(i)
		bit_to_check += 1
	return data[0]

def bin_to_num(binary):
	result = 0
	binary.reverse()
	i = 0
	for digit in binary:
		if digit:
			result += 2**i
		i += 1
	return result

def main():
	with open(filename) as f:
		data = parse_file(f)
		oxygen_rating_bin = select_oxygen_rating(data.copy())
		if verbose:
			print("Oxygen rating: " + str(oxygen_rating_bin) + "\n")
			print("Data is now:")
			print_data_head(data)
		co2_rating_bin = select_co2_rating(data.copy())
		if verbose:
			print("CO2 rating: " + str(co2_rating_bin) + "\n")
		oxygen_rating = bin_to_num(oxygen_rating_bin)
		if verbose:
			print("Oxygen rating: " + str(oxygen_rating) + "\n")
		co2_rating = bin_to_num(co2_rating_bin)
		if verbose:
			print("CO2 rating: " + str(co2_rating) + "\n")
		print(oxygen_rating * co2_rating)

if __name__ == "__main__":
	main()
