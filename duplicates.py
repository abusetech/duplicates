#!/usr/bin/env python3

import os
import argparse
import hashlib
import collections
import threading
import concurrent.futures
import json

CHUNK_SIZE = 512000
tasks = []

parser = argparse.ArgumentParser(description='Finds duplicate files in one or more directories.')
parser.add_argument('directories', metavar="dirs", default=".", type=str, nargs="+", help="List of directories to search")
parser.add_argument('--workers', dest='num_workers', default=6, type=int, help="Number of worker threads to use")
parser.add_argument('--format', dest='format', choices=["json", "csv"], default="csv", help="Output format to use.")
args = parser.parse_args()

root_dirs = args.directories
num_workers = args.num_workers

dict_lock = threading.Lock()
files_db = collections.defaultdict(list)

def append_dict(md5, path):
    with dict_lock:
        files_db[md5].append(path)

def hash_file(filename):
    hasher = hashlib.new('md5')
    with open(filename, 'rb') as file:
        data = file.read(CHUNK_SIZE)
        while len(data) > 0:
            hasher.update(data)
            data = file.read(CHUNK_SIZE)
    return str(hasher.hexdigest())

def hashing_task(path):
    md5 = hash_file(fullpath)
    files_db[md5].append(fullpath)

tpe = concurrent.futures.ThreadPoolExecutor(max_workers=num_workers)
for root_dir in root_dirs:
    for (root, directories, filenames) in os.walk(root_dir):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            tpe.submit(hashing_task(fullpath))

output_string = ""
if args.format == "csv":
    for md5hash in files_db:
        if len(files_db[md5hash]) > 1:
            output_string += os.linesep + files_db[md5hash][0]
            for path in files_db[md5hash][1:]:
                output_string += ", " + path
elif args.format == "json":
    #JSON list-of-lists
    dir_list = []
    for md5hash in files_db:
        if len(files_db[md5hash]) > 1:
            dir_list.append(files_db[md5hash])
    output_string = json.dumps(dir_list)

print(output_string)
