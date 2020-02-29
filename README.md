# Duplicates
A small Python program for finding duplicate files

Usage: duplicates.py [-h] [--workers NUM_WORKERS] dirs [dirs ...]

NUM\_WORKERS	Number of worker threads to use (default: 6)
dirs		A list of directories to search

Duplicates walks the directories in dirs and computes the md5 hash of each file. 
