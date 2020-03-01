# Duplicates
A small Python program for finding duplicate files

Duplicates recursively walks one or more directories, computes the md5 hash of each file in those directories and print a list of of files with identical hashes.

    Usage: duplicates.py [-h] [--workers NUM_WORKERS] [--format {json,csv}] dirs [dirs ...]

__workers:__ Number of worker threads to use (default: 6)

__format:__ Output format to use.
* "json" will output a list of lists of identical files
* "csv" will output line deliminated lists of comma separated values.

__dirs:__ A list of directories to search


