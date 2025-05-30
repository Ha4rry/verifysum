#!/usr/bin/env python3

import os
import sys
import hashlib

class Colours: # thx blender code from stack overflow :D
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

supported_sums = ["sha256", "sha512", "sha1", "md5"]
script_name = sys.argv[0]
try:
    file_path = sys.argv[1]
    sum_type = sys.argv[2].lower()
    provided_checksum = sys.argv[3].lower()
except IndexError:
    raise ValueError(f"Three arguments expected. USAGE: {script_name} [FILE] [CHECKSUM TYPE] [CHECKSUM TO VERIFY]")
if sum_type not in supported_sums:
    raise ValueError(f"Checksum type {sum_type} invalid. Must be an option from {supported_sums}")

if sum_type == "sha256":
    sum_func = hashlib.sha256
elif sum_type == "sha512":
    sum_func = hashlib.sha512
elif sum_type == "sha1":
    sum_func = hashlib.sha1
elif sum_type == "md5":
    sum_func = hashlib.md5

with open(file_path, "rb") as f:
    real_checksum = sum_func(f.read(), usedforsecurity=True).hexdigest().lower()


if real_checksum == provided_checksum:
    print(f"{Colours.OKGREEN}Checksums match. Yay!{Colours.ENDC}")
else:
    print(f"{Colours.FAIL}Checksums do not match. Oh No.{Colours.ENDC}")
