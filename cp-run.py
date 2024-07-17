#! /usr/bin/python3
# for competitive programing

import os, sys

try:
	file_name = sys.argv[1]
	program, file_type = map(str, file_name.split('.'))
	path = '~/Documents/CP/'
	if file_type == 'cpp':
		cpp = f"clang++ -std=c++20 {file_name} -o {program} && timeout 4s ./{program}<{path}inputf.txt>{path}outputf.txt"
		try:
			os.system(cpp)
			print("Worked!")
		except:
			print("Failed! CPP")
	else:
		py = f"timeout 4s python3 {file_name} <{path}inputf.txt>{path}outputf.txt"
		try:
			os.system(py)
			print("Worked!")
		except:
			print("Failed!")
except:
	print("Failed!")
