## Get music library stats to answer existing questions
## - Number of files
## - Number/Frequencies of all file extension types

import argparse
import os
import pandas as pd

# Declare global output variable
output_dict = {}

def parse_dict(extension):
	"""
	Parses a file extension (string) into the output dict. 
	If the file extension is already in the dict, it adds one, 
	if it is a new extension, it creates a new key with a value of 1
	
	Parameters
	----------
	extension : string
		The file extension being parsed into the dict

	Returns
	----------
	Modifys the `output_dict` object in place, does not output anything.
	"""

	# Tell python to refer to the existing global variable within this def
	global output_dict
	if extension in output_dict.keys():
		output_dict[extension] += 1
	else:
		output_dict[extension] = 1

def count_exts():
	"""
	Reads through a predetermined file path, collects all file extensions
	and adds them to an output dict and prints out the key value pairs in the dict

	Parameters
	----------
	None

	Returns
	----------
	out_value : str
		The `output_dict` object, parsed to show each key value pair as a line.
	"""

	mypath = "L:\DeathStar\Music\Music"

	for dirpath, dirnames, filenames in os.walk(mypath):
		if filenames:
			for file in filenames:
				file_ext = os.path.splitext(file)[1]
				parse_dict(file_ext)

	
	for key in output_dict:
		print("{}: {}".format(key, output_dict[key]))
	

## Have to hard code the names of the available tasks to list in the argparser help/description
tasks_available = ["extension_count"]


arg_parser = argparse.ArgumentParser(description='A collection of helpful tasks to build this project')



arg_parser.add_argument('task', metavar='task', type=str, help='The task to execute. Available tasks:\n{}'.format("\n".join(tasks_available)))

args = arg_parser.parse_args()

if args.task not in tasks_available:
	print("You need to specify a valid task. Available tasks are:\n{}".format("\n".join(tasks_available)))
elif args.task == "extension_count":
	count_exts()

