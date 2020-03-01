# Duplicates
A small Python program for finding duplicate files

usage: duplicates.py [-h] [--workers NUM_WORKERS] [--format {json,csv}]
                     dirs [dirs ...]

NUM\_WORKERS	Number of worker threads to use (default: 6)
format		Output format to use.
		"json" will output a list of lists of identical files
		"csv" will output line deliminated lists of comma separated values.
dirs		A list of directories to search

Duplicates walks the directories in dirs and computes the md5 hash of each file. 
